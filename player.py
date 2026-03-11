import time
import math
from items import guns

class Player():
    def __init__(self, health, weapon, tot_currency=None, inventory=None):
        self.health = health
        self.tot_currency = tot_currency if tot_currency is not None else 0
        self.inventory = inventory if inventory is not None else []
        self.weapon = weapon

player = Player(math.inf, guns[0], guns[0], math.inf)

def legendary_item_found(player):
    if player.weapon == True:
        print(f"you have acquired",
          time.sleep(3), "....",
          time.sleep(5), "......",
          time.sleep(8), "{player.inventory}")