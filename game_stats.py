from scoreboard import Scoreboard


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
        with open(self.filename, 'r') as file_objet:
            self.high_score = int(file_objet.read())

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def save(self):
        """对最高分进行存储操作"""
        with open(self.filename, 'w') as file_object:
            file_object.write(str(self.high_score))

    def delete(self):
        """对最高分进行重置操作"""
        self.high_score = 0
        with open(self.filename, 'w') as file_object:
            file_object.write(str(0))
