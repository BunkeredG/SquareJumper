class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800

        # sets each cell to a certain width and height (50 by 50)
        self.cell_width_division = 28
        self.cell_height_division = 16
        self.cell_width, self.cell_height = self.screen_width//self.cell_width_division, self.screen_height//self.cell_height_division

        # sets player values
        self.player_speed = 9
        self.player_color = (255, 255, 255)
        self.player_jump_height = 15
        self.gravity = 1

        # colors
        self.colored_block_color = (255, 0, 0, 30)
        self.text_color = (255, 255, 255)
        self.red_color = (255, 0, 0)

        # allow or disable double jump depending on level
        self.total_double_jumps = [0, 0, 0, 10000, 10000, 1, 10000, 2] # 10000 = infinite

        # movement and movement speed for x direction moving blocks
        self.level_movement_x = [0, 0, 0, 0, 0, 0, 500, 250]
        self.movement_speed_x = [0, 0, 0, 0, 0, 0, 5, 3]

        # movement and movement speed for y direction moving blocks
        self.level_movement_y = [0, 0, 0, 0, 0, 0, 0, 300]
        self.movement_speed_y = [0, 0, 0, 0, 0, 0, 0, 2]

        # level split:
        # 12 total
        # 3 initial with no double jump
        # 3 initial with double jump
        # 2 initial with moving blocks
        # 4 hard combinations

        # list of levels, key on right
        self.levels = [[  # 16 rows, 28 cols, 1 cell is 50x50
            '                           X', # P = Player
            '                           X', # K = Key
            '                           X', # X = Platform
            '                           X', # E = Exit
            '                           X', # D = Death
            ' P                         X', # M = Moving Platform
            'XXX                        E',
            '       XXX   XXX            ', # Level 1, Intro to Game 1
            '                         XXX',
            '                    XXX    X',
            '                           X',
            '          K    XXX         X',
            '  XXX    XXX               X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X', # Level 2, Intro to Game 2
            '                K          X',
            '                           X',
            '                           X',
            '              X     X      X',
            '      X                    X',
            '                  X        X',
            '  X                        E',
            '             XX             ',
            '     XX                   XX',
            ' P                         X',
            'XXX                        X',
            '                           X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X', # Level 3, Intro to Game 3
            '                           X',
            ' K                         X',
            '                           X',
            '                           X',
            '                           X',
            'DD    X    X               X',
            'XX                    X    E',
            '   X             X          ',
            '      X                   XX',
            '          XX               X',
            '                           X',
            '      X                    X',
            ' P                         X',
            'XXX                         X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '               K           X', # Level 4, Intro to Double Jump 1
            '                           X',
            '                           X',
            '                           X',
            '                           X',
            '                     XXX   X',
            '                           X',
            '                           E',
            '                            ',
            ' P                       XXX',
            'XXX                        X',
            '                           X',
            '              XXXXXX       X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X', # Level 5, Intro to Multiple Keys
            '                         K X',
            '                         XXX',
            '                           X',
            'K                  X       X',
            'XX                         X',
            '                           X',
            '                           E',
            '               XX           ',
            '      X                   XX',
            '                           X',
            '                           X',
            '                           X',
            ' P       XX                X',
            'XXX                        X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X', # Level 6, Intro to Limited Double Jumps (incomplete)
            '                           X',
            ' K                         X',
            ' XX     XXXX               E',
            '                            ',
            '               X          XX',
            '                       XX  X',
            '                   X       X',
            '                XXXX       X',
            ' P                         X',
            'XXX                        X',
            '      XXX                  X',
            '                           X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X', # Level 7, Intro to Moving Blocks 1
            'K                          X',
            'XX                         X',
            '       MMMMM               X',
            '                           X',
            '                           X',
            '                         XXX',
            '                           E',
            '                            ',
            '       MMMMM             XXX',
            '                           X',
            ' P                         X',
            'XXX                        X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '            K              X', # Level 8, Intro to Moving Blocks 2 (incomplete)
            '                           X',
            '                           X',
            '                  VVV      X',
            '      MMM                  X',
            '                           X',
            '                        VVVX',
            '                           E',
            '     MMM                    ',
            '                           X',
            '                           X',
            '                           X',
            '    MMM                    X',
            ' P                         X',
            'XXX                        X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            'C'
        ]]

        # number of levels
        self.num_levels = len(self.levels) - 1