from abc import abstractmethod
from items.Weapon import Weapon

# all pistol part stat effects encoded somewhere


class Sniper(Weapon):
    
    # static member variables, same for all objects of this class
    
    # body grip barrel stock accessory sight


    def __init__(self):
        # instance variables
        print("Made a Sniper")
        pass
    


    # interface methods
    def display(self):
        pass