## Player Contents:

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
            3. inventory is intentionally not in here as it is an empty list if not None since we predefined it in the class structurew