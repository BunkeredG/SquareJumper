import pygame
from pygame.sprite import Sprite

# is only a box of art, provides no other value

class SpriteBox(Sprite):
    def __init__(self, game, x, y, spriteURL):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import screen and settings from main.py
        self.settings = game.settings

        # set width and height equal to one cell (50x50)
        self.width, self.height = self.settings.cell_width, self.settings.cell_height

        # load block image
        self.image_path = spriteURL
        self.image = pygame.image.load(self.image_path)

        # create rectangle and set it to a given x and y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y