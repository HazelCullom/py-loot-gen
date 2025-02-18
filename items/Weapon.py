from abc import abstractmethod
from items.LootItem import LootItem

class Weapon(LootItem):
    
    # static member variables, same for all objects of this class



    def __init__(self):
        # instance variables
        pass

    def is_weapon():
        return True

    # interface methods
    @abstractmethod
    def display(self):
        pass