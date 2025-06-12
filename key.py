import pygame
from pygame.sprite import Sprite

class Key(Sprite):
    def __init__(self, game, x, y):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import settings from main.py
        self.settings = game.settings

        # set width and height equal to one cell (50x50)
        self.width, self.height = self.settings.cell_width, self.settings.cell_height

        # load key image
        self.image_path = 'Platformer/key.png'
        self.image = pygame.image.load(self.image_path)

        # create rectangle and set it to a given x and y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y