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

        # allow or disable double jump depending on level
        self.allow_double_jump_list = [False, False, False, True, True, True]

        self.level_movement = [0, 0, 0, 0, 0, 500]
        self.movement_speed = [0, 0, 0, 0, 0, 5]

        # list of levels, key on right
        self.levels = [[  # 16 rows, 28 cols, 1 cell is 50x50
            '                           X', # P = Player
            '                           X', # K = Key
            '                           X', # X = Platform
            '                           X', # E = Exit
            '                           X', # D = Death
            ' P                         X', # M = Moving Platform
            'XXX                        E',
            '       XXX                  ',
            '             XXX         XXX',
            '                    XXX    X',
            '                           X',
            '          K    XXX         X',
            '  XXX    XXX               X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '                           X',
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
            '                           X',
            '                           X',
            ' K                         X',
            '                           X',
            '                           X',
            '                           X',
            'DD   X     X               X',
            'XX                    X    E',
            '   X             X          ',
            '      X                   XX',
            '           X               X',
            '                           X',
            '      X                    X',
            'P                          X',
            'XX                          X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '            K              X',
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
            '            K              X',
            '                           X',
            '                           X',
            '                           X',
            '                           X',
            '                     XXX   X',
            '                           X',
            '                           E',
            '                            ',
            ' P       XXXXXXXXXXX     XXX',
            'XXX                        X',
            '                           X',
            '                           X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            '            K              X',
            '                           X',
            '                           X',
            '                           X',
            '                           X',
            '                     XXX   X',
            '                           X',
            '                           E',
            '       MMMMM                ',
            ' P                       XXX',
            'XXX                        X',
            '                           X',
            '                           X',
            '                           X',
            '                           X',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDX'
        ], [
            'C'
        ]]

        # number of levels
        self.num_levels = len(self.levels) - 1