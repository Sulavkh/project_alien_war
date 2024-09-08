import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class to represent single alien"""

    def __init__(self, aw_game):
        """ initialize the alient at starting point"""
        super().__init__()
        self.screen = aw_game.screen
        self.settings = aw_game.settings

        #load alien image and set rect attribute
        self.image = pygame.image.load('images/enemyship.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)  

    def update(self):
        """move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x