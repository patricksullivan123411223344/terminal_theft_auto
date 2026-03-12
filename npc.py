import math
import ollama 

class NPC():
    def __init__(self, name, health, occupation, status, currency, is_LLM=False):
        self.name = name
        self.health = health
        self.occupation = occupation
        self.status = status
        self.currency = currency
        self.is_LLM = is_LLM

StoreClerk = NPC("Bobby Walnut", 100, "Store Manager", [], 100000)
RegularNPC = NPC("Some Guy", 100, "Probably something lame", [], 100)

all_regular_npcs = [
    StoreClerk,
    RegularNPC
]





