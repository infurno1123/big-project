#This defines the character "class", compiling all the information of said character.
FGO_MAX_LEVELS= {
    1: 60,
    2: 65,
    3: 70,
    4: 80,
    5: 90
    }

class Character:
    def __init__(self, name, game, level, rarity, element, role):
        self.name = name
        self.game = game
        self.level = level
        self.rarity = rarity
        self.element = element
        self.role = role

#If statement that detects game and sets a proper max level according to the information given.

        if self.game == "HSR":
             self.max_level = 80

        elif self.game == "ZZZ":
             self.max_level = 60

        elif self.game == "Endfield":
             self.max_level = 90

        elif self.game == "FGO":
            self.max_level = FGO_MAX_LEVELS[self.rarity]
        else:
             self.max_level = 100

#Level validation here to ensure no weird numbers are given
        if self.level > self.max_level:
             raise ValueError(f"Error: Given Level higher than Max Level for {self.game}!")

#Display is a function that returns a formatted version of the given data for readability
    def display(self):
            return(
                 f"Name: {self.name}\n"
                 f"Game: {self.game}\n"
                 f"Level: {self.level}/{self.max_level}\n"
                 f"Rarity: {self.rarity}★\n"
                 f"Element: {self.element}\n"
                 f"Role: {self.role}\n"
                
            )
#Smaller function that serves as an interactive method of leveling up a character.
    def level_up(self):
        if self.level >= self.max_level:
            print(f"{self.name} is already at max level!")
        else:
            self.level += 1
            print(f"{self.name} has leveled up to {self.level}!")