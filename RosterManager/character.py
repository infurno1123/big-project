#This defines the character "class", compiling all the information of said character.
class Character:
    def __init__(self, name, game, level, rarity, element, role):
        self.name = name
        self.game = game
        self.level = level
        self.rarity = rarity
        self.element = element
        self.role = role

    def display(self):
            print("-"*30)
            print("Name:", self.name)
            print("Game:", self.game)
            print("Level:", self.level)
            print("Rarity:", str(self.rarity) + "★")
            print("Element:", self.element)
            print("Role:", self.role)
            print("-"*30)

welt = Character("Welt", "HSR", 80, 5, "Imaginary", "Delay Specialist")

welt.display()