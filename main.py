import pygame
import sys

from block import Block
from colored_block import ColoredBlock
from death_collider import DeathCollider
from door import Door
from empty_collider import EmptyCollider
from key import Key
from moving_block import MovingBlock
from player import Player
from settings import Settings
from stats import Stats

# Loading background music
# pygame.mixer.init()
# pygame.mixer.music.load('Platformer/Background.mp3')
# pygame.mixer.music.play(-1) # Play the background music on loop
# pygame.mixer.music.set_volume(0.03)

class Platformer:
    def __init__(self):
        pygame.init()

        # large font used for level number display
        self.font = pygame.font.SysFont(None, 50)

        # initialize sound effects
        # self.key_sound = pygame.mixer.Sound('Platformer/Key Collection.mp3')
        # self.key_sound.set_volume(0.05)

        # settings and stats
        self.settings = Settings()
        self.stats = Stats(self)

        # creates the screen with given width and height. vsync is enabled to prevent screentear
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              pygame.SCALED | pygame.DOUBLEBUF, vsync=1)

        # sprite groups
        self.keys = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.moving_blocks = pygame.sprite.Group()
        self.colored_blocks = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.colliders = pygame.sprite.Group()
        self.death_colliders = pygame.sprite.Group()

        # stats
        self.current_level = self.stats.get_stat("level")
        self.num_jumps = self.stats.get_stat("jumps")
        self.num_fails = self.stats.get_stat("fails")

        # number of keys in a given level
        self.num_keys = 0

        # game is running
        self.running = True

        # creates clock which runs game at a certain frame rate
        self.clock = pygame.time.Clock()

        # creates level
        self.create_level()

    def run_game(self):
        while self.running:
            # checks for player input
            self.check_events()

            # moves the player
            self.update_sprites()
            
            # checks collisions between objects and player
            self.check_collisions()

            # draws sprites in their updated positions
            self.update_screen()

            self.move_moving_blocks()
            
            # shows updated drawings on the screen
            pygame.display.flip()

            # ensures the game runs at a set frame rate
            self.clock.tick(60)

    def check_collisions(self):
        # checks collisions between the player and all necessary objects
        self.check_block_player_collision()
        self.move_player_on_moving_block()
        self.check_key_player_collision()
        self.check_door_player_collision()
        self.check_collider_player_collision()
        self.check_death_player_collision()

    def update_sprites(self):
        self.player.update()

    def update_screen(self):
        # fills the background
        self.screen.fill((0, 0, 0))

        # draws all sprites
        self.blocks.draw(self.screen)
        self.colored_blocks.draw(self.screen)
        self.moving_blocks.draw(self.screen)
        self.keys.draw(self.screen)
        self.doors.draw(self.screen)
        self.death_colliders.draw(self.screen)
        self.colliders.draw(self.screen)
        self.player.draw()

        # draws the current level
        self.display_level()

    def create_level(self):
        # remove all objects (includes settings num_keys to 0)
        self.remove_all()

        # for each row (also gets the index of the row)
        for row_idx, row in enumerate(self.settings.levels[self.current_level]):
            # for each cell in row (also gets the index of the cell)
            for cell_idx, cell in enumerate(row):
                # draws a block
                if cell == 'X':
                    self.create_block(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # draws a key
                elif cell == 'K':
                    self.create_key(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # draws a door
                elif cell == 'E':
                    self.create_door(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # draws the player
                elif cell == 'P':
                    self.create_player(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # draws a death collider
                elif cell == 'D':
                    self.create_death_collider(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # draws a moving block
                elif cell == 'M':
                    self.create_moving_block(cell_idx * self.settings.cell_width, row_idx * self.settings.cell_height)

                # close game on completion
                elif cell == 'C':
                    print("\n\n\n\n---COMPLETE---")
                    print("Fails:", self.num_fails)
                    print("Jumps:", self.num_jumps)
                    print("\n\n")
                    self.game_exit()
        
        # allow or deny player the ablility to double jump based off list
        self.player.allow_double_jump = self.settings.allow_double_jump_list[self.current_level]


    def display_level(self):
        # renders the text
        self.level_display = self.font.render(str(self.current_level+1), True, self.settings.text_color)

        # creates and positions the text's rectangle
        self.level_display_rect = self.level_display.get_rect()
        self.level_display_rect.x = 25
        self.level_display_rect.y = 25

        # displays the text
        self.screen.blit(self.level_display, self.level_display_rect)

    
    def create_block(self, x, y):
        new_block = Block(self, x, y)
        self.blocks.add(new_block)

    
    def create_moving_block(self, x, y):
        new_moving_block = MovingBlock(self, x, y)
        self.moving_blocks.add(new_moving_block)

        new_colored_block = ColoredBlock(self, x, y)
        self.colored_blocks.add(new_colored_block)

        dest_colored_block = ColoredBlock(self, x+self.settings.level_movement[self.current_level], y)
        self.colored_blocks.add(dest_colored_block)


    def create_key(self, x, y):
        new_key = Key(self, x, y)
        self.num_keys += 1 # adds 1 to a variable which keeps track of the keys in a level
        self.keys.add(new_key)


    def create_door(self, x, y):
        new_door = Door(self, x, y)
        self.doors.add(new_door)


    def create_death_collider(self, x, y):
        new_collider = DeathCollider(self, x, y)
        self.death_colliders.add(new_collider)

    
    def create_player(self, x, y):
        self.player = Player(self, x, y)

    
    def check_block_player_collision(self):
        # list of all collisions between player and block
        collisions = pygame.sprite.spritecollide(self.player, self.blocks, False)
        moving_collisions = pygame.sprite.spritecollide(self.player, self.moving_blocks, False)

        collisions += moving_collisions

        # if there was a collision
        if collisions:
            # players current coordinates
            p_x = self.player.rect.x
            p_y = self.player.rect.y

            for block in collisions:
                # current block's coordinates
                b_x = block.rect.x
                b_y = block.rect.y

                # if player is directly above
                if b_y <= p_y + self.settings.cell_height < b_y + self.settings.cell_height and b_x - (self.settings.cell_width-10) < p_x < b_x + (self.settings.cell_width-10):
                    # makes player stop moving and pushes player out of the block
                    self.player.change_y = 0
                    self.player.rect.y = b_y - self.settings.cell_height

                    # return jumps to player after landing on ground
                    self.player.on_ground = True
                    self.player.double_jump = True

                    # if player colliding with a moving block (therefore: if player is on top of a moving block)
                    if moving_collisions:
                        self.on_moving_block = True
                
                # if player is below
                elif b_y - self.settings.player_jump_height < p_y - self.settings.cell_height <= b_y and b_x - (self.settings.cell_width-10) < p_x < b_x + (self.settings.cell_width-10):
                    # makes player stop moving and pushes player out of the block
                    self.player.change_y = 0
                    self.player.rect.y = b_y + self.settings.cell_height

                    self.player.on_ground = False

                # if player is to the right
                elif b_x - 20 < p_x - self.settings.cell_width <= b_x and b_y - (self.settings.cell_height-10) < p_y < b_y + (self.settings.cell_height-10):
                    # makes player stop moving and pushes player out of the block
                    self.player.change_x = 0
                    self.player.rect.x = b_x + self.settings.cell_width

                    self.player.on_ground = False

                # if player is to the left
                elif b_x < p_x + self.settings.cell_width <= b_x + self.settings.cell_width and b_y - (self.settings.cell_height-10) < p_y < b_y + (self.settings.cell_height-10):
                    # makes player stop moving and pushes player out of the block
                    self.player.change_x = 0
                    self.player.rect.x = b_x - self.settings.cell_width

                    self.player.on_ground = False

        # if there wasn't a collision with a block, player cannot be on ground
        else:
            self.player.on_ground = False
        
        # if there wasn't a collision with a moving block
        if not moving_collisions:
            self.on_moving_block = False

    
    def move_player_on_moving_block(self):
        if self.on_moving_block:
            # move player at: rate of moving blocks on current level * direction of moving block (forward/reverse)
            self.player.rect.x += self.settings.movement_speed[self.current_level] * self.moving_blocks.sprites()[0].get_direction()

    
    def check_key_player_collision(self):
        # list of all collisions between player and key
        collisions = pygame.sprite.spritecollide(self.player, self.keys, True)
        
        # if there was a collision
        if collisions:
            self.num_keys -= 1 # reduce number of keys left in level
            #self.key_sound.play() # plays key collection sound effect

            # opens door if all keys are collected
            if self.num_keys == 0:
                self.open_door()


    def check_collider_player_collision(self):
        # list of all collisions between player and empty_collider
        collisions = pygame.sprite.spritecollide(self.player, self.colliders, False)

        # if there was a collision
        if collisions:
            self.remove_all() # removes all sprites
            self.current_level += 1 # increases level
            self.create_level() # draws next level


    def check_door_player_collision(self):
        # list of all collisions between player and door
        collisions = pygame.sprite.spritecollide(self.player, self.doors, False)

        # if there was a collision
        if collisions:
            for door in collisions:
                # makes player stop moving horizontally and pushes player out of the door
                self.player.change_x = 0
                self.player.rect.x = door.rect.x - 50

            
    def check_death_player_collision(self):
        # list of all collisions between player and death collider
        collisions = pygame.sprite.spritecollide(self.player, self.death_colliders, False)

        # if there was a collision
        if collisions:
            for death_collider in self.death_colliders:
                if self.player.rect.y >= death_collider.rect.y - 30:
                    self.num_fails += 1 # adds 1 to fail stat
                    self.create_level() # restart level


    def move_moving_blocks(self):
        for block in self.moving_blocks:
            block.move(block.init_x + self.settings.level_movement[self.current_level], self.settings.movement_speed[self.current_level])


    def open_door(self):
        # for each door object
        for door in self.doors:
            # add an invisible collider 25 pixels to the right of the door to check for next level reached
            new_collider = EmptyCollider(self, door.rect.x + 25, door.rect.y)
            self.colliders.add(new_collider)

            new_collider = EmptyCollider(self, door.rect.x + 25, door.rect.y + self.settings.cell_height)
            self.colliders.add(new_collider)

        # removes all door sprites
        self.doors.empty()

    
    def remove_all(self):
        # empties all sprite lists
        self.blocks.empty()
        self.moving_blocks.empty()
        self.colored_blocks.empty()
        self.keys.empty()
        self.doors.empty()
        self.death_colliders.empty()
        self.colliders.empty()

        # clear num_keys
        self.num_keys = 0


    def game_exit(self):
        self.stats.send_stats(self.current_level, self.num_jumps, self.num_fails) # sends current level to a save file
        
        pygame.quit() # stops all modules
        sys.exit() # quits program


    def check_events(self):
        # handle key press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close window (x) pressed
                self.game_exit()

            # if key pressed
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            # if key unpressed        
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keyup_events(self, event):
        # stop moving player left or right
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = False

        # stop player jumping    
        elif event.key == pygame.K_UP:
            self.player.jumping = False

    def check_keydown_events(self, event):
        # move player left, right, or jump
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:  # only jumps once
            self.player.jumping = True

        # quit game on Q pressed
        elif event.key == pygame.K_q:
            self.game_exit()

        # restart game on R presesd
        elif event.key == pygame.K_r:
            self.stats.reset_stats() # resets stats

            # resets variables
            self.current_level = self.stats.get_stat("level")
            self.num_jumps = self.stats.get_stat("jumps")
            self.num_fails = self.stats.get_stat("fails")
            
            self.create_level() # creates level 1


# calls class and runs program
if __name__ == '__main__':
    platformer = Platformer()
    platformer.run_game()