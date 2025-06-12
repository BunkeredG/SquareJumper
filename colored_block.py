import pygame
from pygame.sprite import Sprite

class ColoredBlock(Sprite):
    def __init__(self, game, x, y):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import screen and settings from main.py
        self.settings = game.settings

        # set width and height equal to one cell (50x50)
        self.width, self.height = self.settings.cell_width, self.settings.cell_height

        # create and display rectangle
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image.fill(self.settings.colored_block_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y