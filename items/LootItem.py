from abc import abstractmethod
from items.Item import Item

class LootItem(Item):
    
    # static member variables, same for all objects of this class



    def __init__(self):
        # instance variables
        
        pass
    

    # interface methods
    @abstractmethod
    def display(self):
        pass