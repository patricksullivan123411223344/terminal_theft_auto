import time
import math
from items import guns, melee 

class Player():
    def __init__(self, health, tot_currency=None, inventory=None):
        self.health = health
        self.tot_currency = tot_currency if tot_currency is not None else 0
        self.inventory = inventory if inventory is not None else []

player = Player(math.inf, math.inf, [])