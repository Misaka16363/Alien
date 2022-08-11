class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200  # 1200
        self.screen_height = 800  # 800
        self.bg_color = (255, 255, 255)  # 230, 230, 230

        # 飞船设置
        self.ship_limit = 3  # 3

        # 子弹设置
        self.bullet_width = 3  # 3
        self.bullet_heigth = 15  # 15
        self.bullet_color = (60, 60, 60)  # 60, 60, 60
        self.bullet_allowed = 3  # 3

        # 外星人设置
        self.fleet_drop_speed = 10  # 10

        # 加快游戏节奏的速度
        self.speedup_scale = 1.5  # 1.5
        # 外星人分数的提高速度
        self.score_scale = 1.5  # 1.5

        self.initialize_dynamic_settings()

        # 撞击后暂停时间
        self.sleep_time = 1  # 1

    def initialize_dynamic_settings(self):
        """"初始化随游戏进行而变化的设置"""
        self.ship_speed = 3.0  # 3.0
        self.bullet_speed = 5.0  # 5.0
        self.alien_speed = 2.0  # 2.0

        # 1 表示向右移 -1 表示向左移
        self.fleet_direction = 1  # 1

        # 记分
        self.alien_points = 50  # 50

    def increase_speed(self):
        """提高速度设置和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
