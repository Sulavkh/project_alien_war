class GameStats:
    """Track statistics for Alien War."""
    
    def __init__(self, aw_game):
        """Initialize statistics."""
        self.settings = aw_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit