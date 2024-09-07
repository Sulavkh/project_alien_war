import pygame

class Ship:
    """class to manage the ship"""

    def __init__(self, aw_game):
        """initialize ship and set starting position"""
        self.screen = aw_game.screen
        self.screen_rect = aw_game.screen.get_rect()

        #load ship image
        self.image = pygame.image.load('images/playership.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
