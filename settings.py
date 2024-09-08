class Settings:
    """store all the settings for the project"""

    def __init__(self):
        """initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (86, 86, 86)

        #Ship settings
        self.ship_speed = 4.5

        #bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (253, 0, 0)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1