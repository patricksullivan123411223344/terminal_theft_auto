<<<<<<< HEAD
"""

THIS FILE WILL HOLD ALL ITEMS INSIDE OF THE GAME INCLUDING ITEMS SOLD INSIDE OF THE SHOP!

"""
import math

## WEAPONS
=======
import math

## WEAPONS CLASSES + OBJECTS
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18
class Weapons():
    def __init__(self, name, value=None, legendary = None):
        self.name = name
        self.legendary = legendary if legendary is not None else True
        self.value = value if value is not None else 0

class Guns(Weapons):
<<<<<<< HEAD
    def __init__(self, name, damage, ammo, value, legendary=False):
          super().__init__(name, value, legendary)
          self.damage = damage
          self.ammo = ammo 
    
    def __str__(self):
        return f"{self.name} | Value: ${self.value} | Legendary: {self.legendary}"
=======
    def __init__(self, name, damage, ammo, value, legendary=None):
          super().__init__(name, value, legendary)
          self.damage = damage
          self.ammo = ammo   
    def __str__(self):
        return f"{self.name} | Value: ${self.value} | Legendary: {self.legendary}"
    def __repr__(self):
        return self.__str__()
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18
    
class Melee(Weapons):
    def __init__(self, name, damage, value, legendary=None):
        super().__init__(name, value, legendary)
<<<<<<< HEAD
        self.damage = damage
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name} | Value: {self.value} | Legendary: {self.legendary}"
=======
        self.damage = damage    
    def __str__(self):
        return f"{self.name} | Value: ${self.value} | Legendary: {self.legendary}"
    def __repr__(self):
        return self.__str__()
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18

# Guns
Glock = Guns("Glock", 15, 25, 500)
Barretta = Guns("Barretta", 18, 20, 600)
<<<<<<< HEAD
THE_DESTROYER_EXCLAMATION_POINT = Guns("THE DESTROYER!!!!!!!", math.inf, 10000000, True)
=======
THE_DESTROYER_EXCLAMATION_POINT = Guns("THE DESTROYER!!!!!!!", math.inf, math.inf, 10000000, True)
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18

# Blunt Objects
Stick = Melee("Stick", 2, 0)
Machete = Melee("Machete", 65, 200)
THE_DESTROYER_MELEE_VERSION_EXCLAMATION_POINT = Melee("THE DESTROYER MELEE VERSION!!!!!!!", math.inf, math.inf, True)

<<<<<<< HEAD
=======
# Iterables of guns and melee objects
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18
guns = [
    Glock,
    Barretta,
    THE_DESTROYER_EXCLAMATION_POINT
]
<<<<<<< HEAD

=======
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18
melee = [
    Stick,
    Machete,
    THE_DESTROYER_MELEE_VERSION_EXCLAMATION_POINT
]

<<<<<<< HEAD
## HEALABLES 

class foodWater():
    def __init__(self, name, healing, value):
        self.name = name
        self.healing = healing
        self.value = value
    
class Food(foodWater):
    def __init__(self, name, healing, value, status=None):
        super().__init__(name, healing, value)
        self.status = status
=======
## HEALING CLASSES + OBJECTS 
class Healables():
    def __init__(self, name, healing_power, value):
        self.name = name
        self.healing_power = healing_power
        self.value = max(0, value)

class Food(Healables):
    def __init__(self, name, healing_power, description, value):
        super().__init__(name, healing_power, value)
        self.description = description
    def __str__(self):
        return f"{self.name} | Description: {self.description} | Healing Power: {self.healing_power} | Value: ${self.value}"
    def __repr__(self):
        return self.__str__()
    
class Syringe(Healables):
    def __init__(self, name, healing_power, description, value):
        super().__init__(name, healing_power, value)
        self.description = description
    def __str__(self):
        return f"{self.name} | Description: {self.description} | Healing Power: {self.healing_power} | Value: ${self.value}"
    def __repr__(self):
        return self.__str__()

# Food
Bread = Food("Bread", 10, "Tastes like..... bread", 10)
Steak = Food("Steak", 25, "Now this is something I'll lose some health for", 60)
GoldenApple = Food("Golden Apple", 75, "Where the hell did this come from?", 500)

# Syringe
TheHealer = Syringe("The Healer", 50, "My body tingles after I take this.....", 150)
TheReviver = Syringe("The Reviver", 100, "I don't even want to know where this came from", 1500)

# Iterables of food and syringe objects 
food_healables = [
    Bread,
    Steak,
    GoldenApple
]
syringe_healables = [
    TheHealer,
    TheReviver
]

## MISC ITEMS 
class Misc():
    def __init__(self, name, value, description):
        self.name = name
        self.value = max(0, value)
        self.description = description 

class Funny(Misc):
    def __init__(self, name, value, description, attribute):
        super().__init__(name, value, description)
        self.attribute = attribute

class LostLetters(Misc):
    def __init__(self, name, value, description, contents):
        super().__init__(name, value, description)
        self.contents = contents

misc = []
    
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18
