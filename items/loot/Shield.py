from abc import abstractmethod
from items.LootItem import LootItem

class Shield(LootItem):
    
    # static member variables, same for all objects of this class



    def __init__(self):
        # instance variables
        """
        Shield Capacity
        Recharge Rate
        
        """
        print("Made a Shield")
        pass
    

    # interface methods
    def display(self):
        pass