#This is responsible for managing the collection of characters.
#Note that this file should only have functions/methods that are used by the MAIN file to complete it's given task
class Roster:
    #where self would be a character roster, nothing more nothing less.
    def __init__(self):
        self.characters = []
    
    #add character is given a return value from main, being a character object
    def add_character(self, character_object):
        self.characters.append(character_object)

# 1. Check if roster is empty.
# 2. If empty, return an empty-roster message.
# 3. Create a variable to hold the final output.
# 4. Loop through every Character object.
# 5. Ask each Character to display itself.
# 6. Add that display to the final output.
# 7. Return the completed output.

    def display_all(self):
        if not self.characters:
            return("Error: Roster is currently empty.")
        all_characters = ""
        for char in self.characters:
            all_characters += f"{char.display()}"
        return(all_characters)
    
# Function should get a name input/variable
# Code should compare variable with every value/string in all_characters
#if there is a match, then that should be the return value
#It's purpose is to simply find the character, nothing more nothing less.

    def find_character(self, name):
        for char in self.characters:
            if name == char.name:
                return(char)
        else:
            return(f"Error {name} does not exist within this roster.")

#Notation practice below
#welt = Character("Welt", "HSR", 80, 5, "Imaginary", "Delay Specialist")

#welt.level_up()
#print(welt.display())