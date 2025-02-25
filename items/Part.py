from operator import add as ADD
from operator import sub as SUB
from operator import mul as MUL
from operator import truediv as DIV


class Part():

    # Lookup table for all parts and stat changes. Grips will have matching bonuses which need to be applied.
    # should put in another file and import 

    # Pistol Grip Stats = {"Bandit": {"Mag Size": (MUL, 1.35), "Reload Time": (MUL, 1.1), "Weapon Spread": (MUL,1.15)}, "Dahl": {"Accuracy Regen": (MUL, 1.1), "Impulse Accuracy": (DIV, 1.15), "Max Accuracy": (MUL, 1.15), "Weapon Damage": (DIV, 1.06)}}
    # Pistol Grip Match Bonus = {"Bandit": {"Mag Size": (ADD,4), "Reload Time": (DIV, 1.3)}, "Dahl", {"Mag Size": (ADD, 3), "Reload Time": (DIV, 1.3)}}

    def __init__(self):
        # instance variables
        print("")
        # part needs information: part type (pistol grip, shotgun barrel, shield accessory, pistol body, etc), rarity (for bodies), name: (Torgue Pistol Grip, Jacobs Rifle Body: Uncommon)
        pass

    # general method to generate all parts needed for a pistol