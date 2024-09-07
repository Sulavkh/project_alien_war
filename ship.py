import pygame

class Ship:
    """class to manage the ship"""

    def __init__(self, aw_game):
        """initialize ship and set starting position"""
        self.screen = aw_game.screen
        self.settings = aw_game.settings
        self.screen_rect = aw_game.screen.get_rect()

        #load ship image
        self.image = pygame.image.load('images/playership.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store float value for ship's horizontal position
        self.x = float(self.rect.x)
        
        #movement flag;start with ship not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag."""
        #Update ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
