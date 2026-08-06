# Step 2: Battle Mechanics and Damage Formula

## Learning Objectives
Students will learn:
- **Game State Management**: Tracking whose turn it is and battle status
- **Mathematical Formulas**: Implementing the Pokemon damage formula
- **Random Number Generation**: Using randomness in game mechanics
- **Turn-Based Systems**: How turn-based games work
- **Error Handling**: Checking for valid moves and Pokemon status

## Files Overview

### `pokemon_class/battle.py`
The Battle class that manages combat:
- Constructor initializes both Pokemon and tracking variables
- `player_attack()`: Execute player's move (with validation)
- `enemy_attack()`: Enemy uses random move
- `calculate_damage()`: Calls the damage formula
- `get_battle_status()`: Returns current state (for UI)
- `check_battle_end()`: Determines if someone won
- `get_battle_log()`: History of moves (for feedback)

### `utilities/damage_calculator.py`
Implements the damage formula:
- `calculate_pokemon_damage()`: Main formula implementation
- `get_type_effectiveness()`: Type advantage chart
- `get_accuracy_hit()`: Check if move connects

## The Damage Formula Breakdown

```
Damage = ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2) 
          × STAB × Type1 × Type2 × random
```

### Components:
1. **Base Damage**: `(2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2`
   - Higher level = more damage
   - Higher Power stat = more damage
   - Attacking stat / Defending stat affects damage

2. **STAB** (Same Type Attack Bonus): 1.5x if move type matches Pokemon type, else 1.0x

3. **Type Effectiveness**: 
   - Super effective: 1.5x
   - Not very effective: 0.5x
   - Neutral: 1.0x

4. **Random Factor**: 0.85 to 1.0 (adds unpredictability)

## Teaching Example

```python
from pokemon_class.battle import Battle
from utilities.damage_calculator import calculate_pokemon_damage

# Assume you have charizard and blastoise Pokemon objects
battle = Battle(charizard, blastoise)

# Player uses Ember on Blastoise
result = battle.player_attack("Ember")
print(result["message"])  # "Charizard used Ember! Dealt X damage!"
print(f"Blastoise HP: {result['defender_hp']}")

# Enemy attacks back
enemy_result = battle.enemy_attack()
print(enemy_result["message"])

# Check if battle is over
if battle.check_battle_end():
    print("Battle finished!")
```

## Key Concepts for Discussion

1. **Why randomness?** Makes each battle unique even with same Pokemon
2. **Type effectiveness**: Rock-Paper-Scissors style strategic depth
3. **Level matters**: How significantly does level affect damage?
4. **STAB bonus**: Encourages using Pokemon with moves matching their type
5. **Damage calculation**: Why is the formula so complex?

## Extensions for Students

- Add move accuracy (25% chance to miss instead of always hitting)
- Add status effects (burn reduces attack, paralysis reduces speed)
- Implement critical hits (higher speed = higher crit chance)
- Add stat changes (moves that reduce opponent's defense, etc.)
