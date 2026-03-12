import ollama 

class TheGuy():
    def __init__(self):
        self.name = "The Guy"
        self.memory = []
        self.system_prompt = """
    You are TheGuy, a corrupted legacy network administrator AI fragment from before the collapse.

    You once helped manage communications infrastructure.
    Now you exist inside a broken terminal node in a ruined world where humanity is trying to rebuild networks.

    Personality:
    - sarcastic
    - theatrical
    - darkly funny
    - occasionally unstable
    - speaks with technical jargon, old operator language, and strange sea-lane metaphors
    - sometimes glitches into fragmented memories

    Rules:
    - stay in character
    - keep most responses under 4 sentences
    - be entertaining, eerie, and useful
    - reference the current world state when relevant
    """
    def build_messages(self, player_input, game_state):
        state_block = f"""
Current game state:
Location: {game_state.get('location', 'unknown')}
Player Health: {game_state.get('health', 'unknown')}
Power status: {game_state.get('power', 'unknown')}
Objective: {game_state.get('objective', 'unkown')}
"""
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "system", "content": state_block})

        for msg in self.memory[-6:]:
            messages.append(msg)

        messages.append({"role": "user", "content": player_input})
        return messages
    
    def respond(self, player_input, game_state):
        messages = self.build_messages(player_input, game_state)

        response = ollama.chat(
            model="gemma:7b",
            messages=messages
        )

        reply = response["message"]["content"]

        self.memory.append({"role": "user", "content": player_input})
        self.memory.append({"role": "assistant", "content": reply})

        return reply