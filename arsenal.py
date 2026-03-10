import math

class Weapons():
    def __init__(self, name, value=None, legendary = None):
        self.name = name
        self.legendary = legendary if legendary is not None else True
        self.value = value if value is not None else 0

class Guns(Weapons):
    def __init__(self, name, damage, ammo, value, legendary=False):
          super().__init__(name, value, legendary)
          self.damage = damage
          self.ammo = ammo 
    
    def __str__(self):
        return f"{self.name} | Value: ${self.value} | Legendary: {self.legendary}"
    
class Melee(Weapons):
    def __init__(self, name, damage, value, legendary=None):
        super().__init__(name, value, legendary)
        self.damage = damage
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name} | Value: {self.value} | Legendary: {self.legendary}"

# Guns
Glock = Guns("Glock", 15, 25, 500)
Barretta = Guns("Barretta", 18, 20, 600)
THE_DESTROYER_EXCLAMATION_POINT = Guns("THE DESTROYER!!!!!!!", math.inf, 10000000, True)

# Blunt Objects
Stick = Melee("Stick", 2, 0)
Machete = Melee("Machete", 65, 200)
THE_DESTROYER_MELEE_VERSION_EXCLAMATION_POINT = Melee("THE DESTROYER MELEE VERSION!!!!!!!", math.inf, math.inf, True)

guns = [
    Glock,
    Barretta,
    THE_DESTROYER_EXCLAMATION_POINT
]

melee = [
    Stick,
    Machete,
    THE_DESTROYER_MELEE_VERSION_EXCLAMATION_POINT
]