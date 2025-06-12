import os

class Stats:
    def __init__(self, game):
        self.settings = game.settings # reference game settings
        self.file_name = "./Platformer/user_stats.txt" # sets name of the stats file

        self.create_stats()
        

    def get_stat(self, stat):
        # opens file and reads the first line
        with open(self.file_name, "r") as file:
            line = file.readline()

        # splits the string into a list of different stats
        lines = line.split()

        # returns the requested stat
        if stat == "level":
            return int(lines[0])
        elif stat == "jumps":
            return int(lines[1])
        elif stat == "fails":
            return int(lines[2])


    def send_stats(self, level, jumps, fails):
        # opens the file and writes each stat with a space in between (useful for the .split function in get_stat)
        with open(self.file_name, 'w') as file:
            file.write(str(level) + " ")
            file.write(str(jumps) + " ")
            file.write(str(fails))

            file.write("\nLEVEL - JUMPS - FAILS") # a redundant line in the text file for quickly remembering which stat is which


    def create_stats(self):
        file_list = os.listdir("./Platformer/") # file_list is a list that contains the title of every file in the Platformer directory
        
        # if the user stats file does not exist
        if "user_stats.txt" not in file_list:

            # creates a new stats file and sets all values to 0
            with open(self.file_name, 'w') as file:
                file.write("0 0 0")
        
        # if the level value in the stats file equals the number of levels, resets the game
        elif self.get_stat("level") >= self.settings.num_levels:
            self.reset_stats()
            

    def reset_stats(self):
        # removes the stats file
        os.remove(self.file_name)

        # creates a new stats file and sets all values to 0
        with open(self.file_name, 'w') as file:
            file.write("0 0 0")