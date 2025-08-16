import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, game, x, y):
        # retrieve initialization function from class Sprite
        super().__init__()

        # import screen from main.py
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.stats = game.stats
        self.screen_rect = self.screen.get_rect()
        self.num_double_jumps = 0

        # creates player rectangle with given width and height at specific position
        self.width, self.height = 50, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        self.rect.x = x
        self.rect.y = y

        # variables to control movement
        self.moving_right = False
        self.moving_left = False
        self.jumping = False

        # booleans for allowing jumps
        self.on_ground = True
        self.double_jump = True

        self.change_x, self.change_y = 0, 0

    # updates player
    def update(self):
        self.calc_grav()


        # stops player from falling after reaching bottom
        if self.rect.y >= self.settings.screen_height - self.height: # bottom of the screen:
            self.rect.y = self.settings.screen_height - self.height # pops player back up above ground
            self.change_y = 0

            # reinstate jumps
            self.on_ground = True
            self.double_jump = True
        
        # checks for keypress and ensures player is not out of bounds
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += self.settings.player_speed
        elif self.moving_left and self.rect.left >= self.settings.player_speed:
            self.rect.x -= self.settings.player_speed

        # if jumping is detected, run jump function
        if self.jumping:
            self.jump()

        self.rect.y += self.change_y

    def calc_grav(self):
        self.change_y += self.settings.gravity # changes y position of player based on self.settings.gravity
        

    def jump(self):
        # if player is on ground
        if self.on_ground:
            self.jump_util()
            self.on_ground = False # player is no longer on the ground
            self.jumping = False # player is no longer jumping

        # if player has an available double jump and there are still double jumps available
        elif self.double_jump and self.num_double_jumps > 0:
            self.jump_util()
            self.num_double_jumps -= 1 # decrease available number of double jumps
            self.double_jump = False # player no longer has a double jump

    
    def jump_util(self):
        self.change_y = -(self.settings.player_jump_height) # perform jump
        self.jumping = False # player is no longer jumping
        self.game.num_jumps += 1 # adds 1 to the "jump" stat


    def draw(self):
        # draws player with given screen, color, and rectangle
        pygame.draw.rect(self.screen, self.settings.player_color, self.rect)
        