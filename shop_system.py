from items import guns, melee
from items import guns, melee, food_healables, syringe_healables
from player import player
from npc import StoreClerk
import time
import sys

def terminalPrintAnimation(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def shoppingLogic():
    shopping_categories = {
        "weapons": guns + melee,
        "healables": food_healables + syringe_healables,
        "misc": []
    }

    terminalPrintAnimation("What would you like to see?")
    for category in shopping_categories:
        terminalPrintAnimation(f"---{category.upper()}---")
    
    classChoice = input("Choose your class for specific items: ").strip().lower()

    if classChoice not in shopping_categories:
        terminalPrintAnimation("This category doesn't exist yet! But it may soon...")
        return None
    
    selected_items = shopping_categories[classChoice]

    if not selected_items:
        terminalPrintAnimation("This category is empty...... for now")
        return None
    
    terminalPrintAnimation(f"\n---{classChoice.upper()}---")
    for i, item in enumerate(selected_items, 1):
        terminalPrintAnimation(f"{i}, {item}")

    itemChoice = input("Choose item number: ").strip()

    if not itemChoice.isdigit():
        terminalPrintAnimation("Invalid item number...")
        return None
    
    itemIndex = int(itemChoice) - 1

    if not (0 <= itemIndex < len(selected_items)):
        terminalPrintAnimation("That item does not exist...")
        return None
    
    return selected_items[itemIndex]

terminalPrintAnimation(str("Welcome to the shop!"))
time.sleep(1)
terminalPrintAnimation("To continue shopping, type SHOP")
time.sleep(1)
terminalPrintAnimation("To see our stock, type STOCK")
time.sleep(1)
player_choice = input("What would you like to do?: ")

if player_choice == "":
    raise ValueError("The player should answer with either SHOP or STOCK...")
    sys.exit()

if player_choice == "STOCK":
    terminalPrintAnimation("Heres what we have:")
    terminalPrintAnimation("\n--- GUNS ---")
    for weapon in guns:
        terminalPrintAnimation(str(weapon))
    terminalPrintAnimation("\n--- MELEE ---")
    for weapon in melee:
        terminalPrintAnimation(str(weapon))
    terminalPrintAnimation("\n--- FOOD ---")
    for food in food_healables:
        terminalPrintAnimation(str(food))
    terminalPrintAnimation("\n--- SYRINGE ---")
    for syringe in syringe_healables:
        terminalPrintAnimation(str(syringe))

player_choice = input("So... ready to shop? (Y/N): ")

if player_choice == "Y":
    chosenItem = shoppingLogic()
    if chosenItem:
        player.inventory.append(chosenItem)
        terminalPrintAnimation(f"{chosenItem.name} has been added to your inventory. Congrats... I think?")
elif player_choice == "N":
    terminalPrintAnimation("See you next time, broke boy...")
    sys.exit()

terminalPrintAnimation(str(player.inventory))