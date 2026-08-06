# Step 1: Pokemon Class and Data Structures

## Learning Objectives
Students will learn:
- **Classes**: Creating a Pokemon class with properties and methods
- **Dictionaries**: Using dictionaries to store moves, stats, and data
- **Lists**: Working with lists of Pokemon and moves
- **Instance Variables**: Understanding attributes and current state (like current_hp)
- **Methods**: Creating methods to interact with Pokemon data

## Files Overview

### `pokemon_class/pokemon.py`
The main Pokemon class containing:
- Constructor (`__init__`) that takes stats and moves
- Instance variables for stats, moves, and current state
- Methods:
  - `is_alive()`: Check if Pokemon has HP > 0
  - `take_damage()`: Reduce HP
  - `heal()`: Restore HP
  - `get_move()`: Retrieve move details
  - `get_all_moves()`: List all available moves

### `utilities/pokemon_data.py`
Database of Pokemon and Moves:
- `MOVES`: Dictionary of all available moves with properties (power, accuracy, type)
- `POKEMON_DATABASE`: Dictionary of Pokemon with their stats and move sets
- `TYPE_EFFECTIVENESS`: Chart showing type advantages
- Helper functions to access data

## Teaching Example

```python
from pokemon_class.pokemon import Pokemon
from utilities.pokemon_data import POKEMON_DATABASE, MOVES

# Create a Charizard using data from our database
char_data = POKEMON_DATABASE["Charizard"]
charizard_moves = {move: MOVES[move] for move in char_data["moves"]}

charizard = Pokemon(
    name="Charizard",
    level=char_data["level"],
    pokemon_type=char_data["type"],
    hp=char_data["hp"],
    attack=char_data["attack"],
    defense=char_data["defense"],
    sp_atk=char_data["sp_atk"],
    speed=char_data["speed"],
    moves=charizard_moves
)

print(charizard)  # Charizard (Lvl. 50) - 78/78 HP
print(charizard.get_all_moves())  # ['Ember', 'Tackle', 'Scratch', 'Pound']
```

## Key Concepts to Discuss

1. **Dictionaries as Databases**: Why use a dictionary for moves instead of separate variables?
2. **Class Attributes vs Instance Variables**: What's the difference?
3. **Methods for State Management**: Why use `take_damage()` instead of directly modifying HP?
4. **Data Organization**: How dictionaries help organize related information

## Discussion Questions for Students

- Why do we store moves as a dictionary instead of a list?
- What would happen if current_hp went below 0? How do we prevent that?
- Could we add more methods to the Pokemon class? What would be useful?
- How would we create a Pokemon from the database?
