import random

class Fighter:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.speed = 5
        self.defense = 3
        self.special = "not implemented"
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, target):
        print(f'{self.name} punches {target.name}')
        target.defend(self.strength)

    def use_special(self):
        self.defense += random.randint(5,10) 
        self.strength += random.randint(5,10)
        self.show_stats()
    
    def defend(self, amount):
        damage = amount - self.defense
        if damage <0:
            damage=0
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f'{self.name} took {damage} and now has {self.health} health')
    
    def power_up(self):
        print(f'{self.name} {self.special}')
        self.show_stats()

    