from classes.fighter import Fighter

class Ninja(Fighter):

    def __init__( self , name ):
        super().__init__(name)
        self.speed +=2
        self.special = "Throws Pizza"

    def power_up(self):
        self.speed += 10
        super().use_special()
        print(f'{self.name}\nDrinking RedBull! Speed +10\n')
    
    def attack(self, target):
        super().attack(target)
        if self.speed >10:
            super().attack(target) 
            super().attack(target)
            
        elif self.speed >20:
            super().attack(target)
            super().attack(target)
            super().attack(target)
            


        
            
        