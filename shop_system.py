from arsenal import guns, melee
from player import player
import time
import sys

print("This is the shop!")
time.sleep(3)
print("To continue shopping, type SHOP")
time.sleep(3)
print("To see our stock, type STOCK")
time.sleep(3)
player_input = input("Whats your move?: ")

if player_input == "":
    raise ValueError("The player should answer with either SHOP or STOCK...")
    sys.exit()

if player_input == "STOCK":
    print("Heres what we have:")
    print(f"{guns[0:3+1]}")
    print(f"{melee[0:3+1]}")