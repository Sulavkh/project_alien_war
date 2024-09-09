class GameStats:
    """Track statistics for Alien War."""
    
    def __init__(self, aw_game):
        """Initialize statistics."""
        self.settings = aw_game.settings
        self.reset_stats()
        #high score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
