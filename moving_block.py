import pygame
from pygame.sprite import Sprite

class MovingBlock(Sprite):
    def __init__(self, game, x, y):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import screen and settings from main.py
        self.settings = game.settings

        # set width and height equal to one cell (50x50)
        self.width, self.height = self.settings.cell_width, self.settings.cell_height

        # load block image
        self.image_path = './block.png'
        self.image = pygame.image.load(self.image_path)

        # create rectangle and set it to a given x and y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = 0
        self.init_x = x

    def move(self, final_x, speed):
        # if final_x is right of initial position
        if self.init_x - final_x < 0:
            # checks for current x in relation to path and changes direction when reaching edge of path
            if self.rect.x <= self.init_x:
                self.direction = 1
            elif self.rect.x >= final_x:
                self.direction = -1
        
        # if final_x is left of initial position
        elif self.init_x - final_x > 0:
            # checks for current x in relation to path and changes direction when reaching edge of path
            if self.rect.x >= self.init_x:
                self.direction = -1
            elif self.rect.x <= final_x:
                self.direction = 1

        self.rect.x += self.direction * speed

    def get_direction(self):
        return self.direction