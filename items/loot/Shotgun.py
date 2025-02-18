from abc import abstractmethod
from items.Weapon import Weapon



class Shotgun(Weapon):
    
    # static member variables, same for all objects of this class



    def __init__(self):
        # instance variables
        print("Made a Shotgun")
        pass
    


    # interface methods
    def display(self):
        pass