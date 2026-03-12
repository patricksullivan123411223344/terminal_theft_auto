## Player:

1. Players and their objects are defined with a class Players()
    - the Players() class uses arguments:
        1. health
        2. tot_currency (total currency)
        3. inventory (set to None initially, if inventory is None else [], an empty list for mutability)

2. Initially, the player starts with:
    - A variable player assigned to Player()
        - Player() holds
            1. health = 100 (as argument one)
            2. currency = 5000 (as argument 2)
            3. inventory is intentionally not in here as it is an empty list if not None since we predefined it in the class structure

## Items

The items section is split up in multiple different classes. They include the following:
1. Weapons:
    - Guns
    - Melee
2. Healing
    - Food
    - Syringe
3. Miscellenious
    - MP3 Player
    - Rocket Fuel (...)
Each section pertains its own class (Weapons, Healing, Miscellenious) with subclasses (guns & melee, food & syringe, mp3 player & rocket fuel)

