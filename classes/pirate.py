from classes.fighter import Fighter

class Pirate(Fighter):

    def __init__( self , name ):
        super().__init__(name)
        self.speed = 3
        self.special= 'Throws Rum bottle'
    
    def power_up(self):
        self.strength += 5
        super().use_special()
        print(f'{self.name}\nEating Spinach! Strength +5\n') 