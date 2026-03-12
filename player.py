import time
import math
<<<<<<< HEAD
from items import guns
=======
from items import guns, melee 
>>>>>>> 7c2306d0c9efc33c8c2df3cd4d4bf4d48b8b9d18

class Player():
    def __init__(self, health, tot_currency=None, inventory=None):
        self.health = health
        self.tot_currency = tot_currency if tot_currency is not None else 0
        self.inventory = inventory if inventory is not None else []

player = Player(math.inf, math.inf, [])