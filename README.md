# Python Loot Generation
A script that attempts to recreate the Borderlands style of generating loot

## Plan
 - Everything is as customizable / dynamic as possible including:
    - drop rates: in separate file, global
    - types of loot
    - any constant value really
    - need a "base weapon stat" formula as a function of level for each item type
        - these stats can then be modified by rarity scaling, individual part contribution, etc

## Data structure ideas
(object oriented approach is maybe not the best for python, but its how I think)
- **LootItem** class
    
    Fields
    - item type: class mod, relic, grenade, shield, pistol, AR, shotgun, rocket launcher, smg
    - partList: dict of parts making up the wep
    - stats: a dict (or its own class) with all stats, like level, rarity, manufacturer, title, description (if applicable: damage, accuracy, fire rate, elemental effect chance, mag size). will be filtered for only relavant stats whenever displayed (this means many stats will be left blank/none for some items, but its nice to have a consistent stats field for all items)
    
    Methods
    - constructor(itemtype=random/weapon/shield/pistol/etc, level=current/givenNum/scaleToCurrent, rarityWeights=even/common/uncommon/rare/epic/legendary/player info based?/etc, forcedParts=none/specificPartID): the main function to generate an item of loot, defaults to random loot, but can be passed in config params to specify type, level, rarity rates, or specic parts. 

- **LootItemType** parent class / interface: just type definition for the item type variable in LootItem
    
    Methods
    - randomItemType()
    - getRelevantStats(): will return some mask or filter to apply to the LootItem "stats" field when displayed to only diplay relavent fields. potentially not necessary if blank fields are set to and checked for "none"

- **Weapon** Interface / parent class: to decide how things are equipped later, can check if item type is a subclass of weapon instead of having a lookup list

    Methods
    - randomWeaponType()

- **Part** class: a part of an item

    Field:
    - parentItemType: a lootItemType for the parent item that this part belongs to
    - partType: pistolGrip/pistolBodyCommon/shieldBodyRare/arBarrel/etc
    - manufacturer: torgue/vladof/bandit/etc
    - statAffect: static lookup table for different parts from different manufacturers and 

- **Element** struct: a defined set of elements (including normal), useful for comparison 