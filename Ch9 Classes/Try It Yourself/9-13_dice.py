import random

class Dice:
    """"""
    
    def __init__(self):
        """"""
        
        self.sides = 6
        
        
    def roll_die(self):
        """"""
        
        print(random.randint(1, self.sides))
        
        
roll_the_dice = Dice()
roll_the_dice.roll_die()