class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态
        self.game_active = False

        # 任何情况下都不应重置最高得分
        self.high_score = 0
        # self.load(self)
        self.filename = 'data'
        try:
            with open(self.filename, 'r') as file_objet:
                try:
                    # 咳咳，这里的加密校验如果被人看到能被笑死
                    # 可以给我发个邮件 i@misaka.contact
                    value = int(file_objet.read()) ^ 20220816377
                    if value % 200507202209 != 0:
                        self.delete()
                    elif value == 0:
                        self.high_score = 0
                    else:
                        self.high_score = int(value / 200507202209)
                except ValueError:
                    self.delete()
        except FileNotFoundError:
            self.delete()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save(self):
        """对最高分进行存储操作"""
        if self.high_score == 0:
            with open(self.filename, 'w') as file_object:
                file_object.write(str(0))
        else:
            with open(self.filename, 'w') as file_object:
                file_object.write(
                    str(((self.high_score) * 200507202209) ^ 20220816377))

    def delete(self):
        """对最高分进行重置操作"""
        self.high_score = 0
        with open(self.filename, 'w') as file_object:
            file_object.write(str(self.high_score))
