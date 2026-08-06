"""
Step 2: Damage Calculator
=========================
Implements the Pokemon damage formula.

Formula: 
    Damage = ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2) 
              × STAB × Type1 × Type2 × random

Teaching concepts:
- Mathematical formulas in code
- Function parameters and return values
- Random number generation
- Order of operations
"""

import random


def calculate_pokemon_damage(attacker, defender, move):
    """
    Calculate damage dealt using the standard Pokemon damage formula.
    
    Args:
        attacker (Pokemon): The attacking Pokemon
        defender (Pokemon): The defending Pokemon
        move (dict): Move dictionary with 'power' key
        
    Returns:
        tuple: (damage, type_effectiveness) where damage is int and type_effectiveness is float
    """
    
    # Extract parameters
    level = attacker.level
    power = move.get("power", 0)
    attack = attacker.sp_atk if move.get("type") == "special" else attacker.attack
    defense = defender.sp_atk if move.get("type") == "special" else defender.defense
    
    # Part 1: Base damage calculation
    # ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2)
    level_factor = (2 * level / 5 + 2)
    stat_factor = attack / defense
    base_damage = (level_factor * power * stat_factor / 50 + 2)
    
    # Part 2: Multipliers
    # STAB = 1.5 if same type as attacker's type, 1.0 otherwise
    stab = 1.5 if move.get("type") == attacker.pokemon_type else 1.0
    
    # Type effectiveness (simplified - Type1 for attacking move type)
    type_effectiveness = get_type_effectiveness(
        move.get("type"), 
        defender.pokemon_type
    )
    
    # Random factor between 0.85 and 1.0 (85% to 100%)
    random_factor = random.uniform(0.85, 1.0)
    
    # Final calculation
    final_damage = base_damage * stab * type_effectiveness * random_factor
    
    # Ensure minimum damage of 1 and return tuple with type effectiveness
    return max(1, int(final_damage)), type_effectiveness


def get_type_effectiveness(attacking_type, defending_type):
    """
    Calculate type effectiveness multiplier.
    
    Args:
        attacking_type (str): Type of move
        defending_type (str): Type of defender
        
    Returns:
        float: Effectiveness multiplier (0.5, 1.0, or 1.5)
    """
    
    # Simplified type chart
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
    
    # Default to 1.0 (neutral) if type not found
    if attacking_type not in type_chart:
        return 1.0
    
    return type_chart[attacking_type].get(defending_type, 1.0)


def get_accuracy_hit(accuracy):
    """
    Determine if a move hits based on accuracy.
    
    Args:
        accuracy (int): Accuracy percentage (0-100)
        
    Returns:
        bool: True if move hits, False if it misses
    """
    return random.random() * 100 < accuracy
