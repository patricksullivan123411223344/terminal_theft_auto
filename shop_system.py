from items import guns, melee
from player import player
import time
import sys

def terminalPrintAnimation(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

terminalPrintAnimation("Welcome to the shop!")
time.sleep(1)
terminalPrintAnimation("To continue shopping, type SHOP")
time.sleep(1)
terminalPrintAnimation("To see our stock, type STOCK")
time.sleep(1)
player_choice = input("SHOP/STOCK: ")

if player_choice == "":
    raise ValueError("The player should answer with either SHOP or STOCK...")
    sys.exit()

if player_choice == "STOCK":
    terminalPrintAnimation("Heres what we have:")
    print(guns)
    time.sleep(0.5)
    print(melee)



