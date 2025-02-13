from abc import ABC, abstractmethod

class Item(ABC):
    
    # static member variables, same for all objects of this class



    def __init__(self):
        # instance variables
        """
        Rarity
        Level
        Name
        """
        pass
    

    # interface methods
    @abstractmethod
    def display(self):
        pass