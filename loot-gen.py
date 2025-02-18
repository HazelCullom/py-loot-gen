import random
import os
import importlib


# code will be here, YAAAAAAAYYYYYYY!!!!!!!

# get all types of loot in a list
LOOT_STRS = [f[:f.find('.')] for f in os.listdir("items/loot") if f[0] != '_']


# get the actual classes in a list
LOOT_CLASSES = {}
for loot_str in LOOT_STRS:
    module = importlib.import_module("items.loot." + loot_str)
    LOOT_CLASSES[loot_str] = getattr(module, loot_str)
    # insntance = LOOT_CLASSES[loot_str]() # used to test that instances are instantiated correctly




def generate_random_loot(whitelist=LOOT_STRS.copy()):

    # pick a random piece of loot
    # call that loot's generate function
    """
    Will need to define loot generation settings, want it to have consistent format for all loot generation functions:
      ideas: 
      just a fuck ton of optional arguments with default values defined somewhere
      json format something or other
    """
    # filter out weapons if user added "Weapon" to whitelist
    if "Weapon" in whitelist:
        for loot_str in LOOT_STRS:
            if LOOT_CLASSES[loot_str].is_weapon():
                whitelist.append(loot_str)

    loot = random.choice(list(filter(lambda s: s in whitelist, LOOT_STRS)))
    instance = LOOT_CLASSES[loot]()
    pass


if __name__ == "__main__":
    print(LOOT_STRS)
    generate_random_loot(whitelist=["Weapon"])
    generate_random_loot(whitelist=["Shield"])