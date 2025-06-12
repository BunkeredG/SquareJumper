import pygame
from pygame.sprite import Sprite

# does not get drawn, is just a collision box

class EmptyCollider(Sprite):
    def __init__(self, game, x, y):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import settings from main.py
        self.settings = game.settings

        # set width and height equal to one cell (50x50)
        self.width, self.height = self.settings.cell_width, self.settings.cell_height

        # create rectangle and set it to a given x and y
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y