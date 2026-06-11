#This is responsible for managing the collection of characters.
#Note that this file should only have functions/methods that are used by the MAIN file to complete it's given task
class Roster:
    #where self would be a character roster, nothing more nothing less.
    def __init__(self):
        self.characters = []
    
    #add character is given a return value from main, being a character object
    def add_character(self, character_object):
        self.characters.append(character_object)
        


#Notation practice below
#welt = Character("Welt", "HSR", 80, 5, "Imaginary", "Delay Specialist")

#welt.level_up()
#print(welt.display())
