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