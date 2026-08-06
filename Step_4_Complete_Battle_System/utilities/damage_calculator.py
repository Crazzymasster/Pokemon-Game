"""
Step 4: Damage Calculator (copied from Step 2)
"""

import random


def calculate_pokemon_damage(attacker, defender, move):
    """
    Calculate damage dealt using the standard Pokemon damage formula.
    Returns a tuple of (damage, type_effectiveness_multiplier)
    """
    
    level = attacker.level
    power = move.get("power", 0)
    attack = attacker.sp_atk if move.get("type") == "special" else attacker.attack
    defense = defender.sp_atk if move.get("type") == "special" else defender.defense
    
    level_factor = (2 * level / 5 + 2)
    stat_factor = attack / defense
    base_damage = (level_factor * power * stat_factor / 50 + 2)
    
    stab = 1.5 if move.get("type") == attacker.pokemon_type else 1.0
    
    type_effectiveness = get_type_effectiveness(
        move.get("type"), 
        defender.pokemon_type
    )
    
    random_factor = random.uniform(0.85, 1.0)
    
    final_damage = base_damage * stab * type_effectiveness * random_factor
    
    return max(1, int(final_damage)), type_effectiveness


def get_type_effectiveness(attacking_type, defending_type):
    """Calculate type effectiveness multiplier."""
    
    type_chart = {
        "fire": {"grass": 1.5, "ice": 1.5, "bug": 1.5, "steel": 1.5, 
                 "water": 0.5, "fire": 0.5, "rock": 0.5},
        "water": {"fire": 1.5, "ground": 1.5, "rock": 1.5, 
                  "water": 0.5, "grass": 0.5, "ice": 0.5},
        "grass": {"water": 1.5, "ground": 1.5, "rock": 1.5, 
                  "grass": 0.5, "fire": 0.5, "ice": 0.5},
        "electric": {"water": 1.5, "flying": 1.5, 
                     "grass": 0.5, "electric": 0.5, "dragon": 0.5},
    }
    
    if attacking_type not in type_chart:
        return 1.0
    
    return type_chart[attacking_type].get(defending_type, 1.0)


def get_accuracy_hit(accuracy):
    """Determine if a move hits based on accuracy."""
    return random.random() * 100 < accuracy
