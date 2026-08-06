"""
Step 4: Pokemon Database (copied from Step 1)
"""

MOVES = {
    "Tackle": {
        "power": 40,
        "accuracy": 100,
        "type": "normal",
        "description": "A physical attack using the body."
    },
    "Ember": {
        "power": 40,
        "accuracy": 100,
        "type": "fire",
        "description": "An attack of small flames."
    },
    "Water Gun": {
        "power": 40,
        "accuracy": 100,
        "type": "water",
        "description": "Squirts water at the foe."
    },
    "Razor Leaf": {
        "power": 55,
        "accuracy": 95,
        "type": "grass",
        "description": "Sharp leaves slice the foe."
    },
    "Thunderbolt": {
        "power": 90,
        "accuracy": 100,
        "type": "electric",
        "description": "A strong electric blast."
    },
    "Bite": {
        "power": 60,
        "accuracy": 100,
        "type": "dark",
        "description": "The foe is bitten with sharp fangs."
    },
    "Pound": {
        "power": 40,
        "accuracy": 100,
        "type": "normal",
        "description": "Pounds the foe with foreleg."
    },
    "Scratch": {
        "power": 40,
        "accuracy": 100,
        "type": "normal",
        "description": "Scratches the foe with sharp claws."
    },
}

POKEMON_DATABASE = {
    "Charizard": {
        "level": 50,
        "type": "fire",
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "sp_atk": 109,
        "speed": 100,
        "moves": ["Ember", "Tackle", "Scratch", "Pound"]
    },
    "Blastoise": {
        "level": 50,
        "type": "water",
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "sp_atk": 109,
        "speed": 78,
        "moves": ["Water Gun", "Tackle", "Bite", "Pound"]
    },
    "Venusaur": {
        "level": 50,
        "type": "grass",
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "sp_atk": 100,
        "speed": 80,
        "moves": ["Razor Leaf", "Tackle", "Scratch", "Pound"]
    },
    "Pikachu": {
        "level": 35,
        "type": "electric",
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "sp_atk": 50,
        "speed": 90,
        "moves": ["Thunderbolt", "Tackle", "Scratch", "Pound"]
    },
    "Dragonite": {
        "level": 55,
        "type": "dragon",
        "hp": 91,
        "attack": 134,
        "defense": 95,
        "sp_atk": 100,
        "speed": 80,
        "moves": ["Pound", "Tackle", "Bite", "Scratch"]
    },
    "Gyarados": {
        "level": 50,
        "type": "water",
        "hp": 95,
        "attack": 125,
        "defense": 79,
        "sp_atk": 60,
        "speed": 81,
        "moves": ["Water Gun", "Bite", "Tackle", "Pound"]
    },
}

TYPE_EFFECTIVENESS = {
    "fire": {"grass": 1.5, "ice": 1.5, "bug": 1.5, "steel": 1.5, "water": 0.5, "fire": 0.5, "rock": 0.5},
    "water": {"fire": 1.5, "ground": 1.5, "rock": 1.5, "water": 0.5, "grass": 0.5, "ice": 0.5},
    "grass": {"water": 1.5, "ground": 1.5, "rock": 1.5, "grass": 0.5, "fire": 0.5, "ice": 0.5},
    "electric": {"water": 1.5, "flying": 1.5, "grass": 0.5, "electric": 0.5, "dragon": 0.5},
    "normal": {"rock": 0.5, "ghost": 0.0},
    "fire": {"grass": 1.5, "ice": 1.5, "bug": 1.5, "steel": 1.5},
    "water": {"fire": 1.5, "ground": 1.5, "rock": 1.5},
    "grass": {"water": 1.5, "ground": 1.5, "rock": 1.5},
}

def get_pokemon_data(pokemon_name):
    return POKEMON_DATABASE.get(pokemon_name, None)

def get_move_data(move_name):
    return MOVES.get(move_name, None)

def get_random_pokemon():
    import random
    return random.choice(list(POKEMON_DATABASE.keys()))
