# Quick Start Guide - Pokemon Battle Game

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pygame library

### Setup

```bash
# Install pygame
pip install pygame
```

---

## 🚀 Running Each Step

### Step 1: Pokemon Class and Data Structures
**What to learn**: Classes, Dictionaries, Object-Oriented Programming

**How to test it**:

Create a test file `test_step1.py`:

```python
import sys
sys.path.insert(0, 'Step_1_Pokemon_Class_and_Data')

from pokemon_class.pokemon import Pokemon
from utilities.pokemon_data import POKEMON_DATABASE, MOVES

# Create Charizard from database
data = POKEMON_DATABASE["Charizard"]
moves_dict = {name: MOVES[name] for name in data["moves"]}

charizard = Pokemon(
    name="Charizard",
    level=data["level"],
    pokemon_type=data["type"],
    hp=data["hp"],
    attack=data["attack"],
    defense=data["defense"],
    sp_atk=data["sp_atk"],
    speed=data["speed"],
    moves=moves_dict
)

# Test the Pokemon
print(charizard)  # Should print: Charizard (Lvl. 50) - 78/78 HP
print(f"Moves: {charizard.get_all_moves()}")

# Test taking damage
charizard.take_damage(30)
print(charizard)  # Should print: Charizard (Lvl. 50) - 48/78 HP

# Test getting a move
ember = charizard.get_move("Ember")
print(f"Ember power: {ember['power']}")  # Should print: Ember power: 40
```

**Run it**:
```bash
python test_step1.py
```

---

### Step 2: Battle Mechanics
**What to learn**: Game Logic, Battle System, Damage Formula

**How to test it**:

Create a test file `test_step2.py`:

```python
import sys
sys.path.insert(0, 'Step_2_Battle_Mechanics')

from pokemon_class.pokemon import Pokemon
from pokemon_class.battle import Battle
from utilities.pokemon_data import POKEMON_DATABASE, MOVES

def create_pokemon(name):
    data = POKEMON_DATABASE[name]
    moves_dict = {m: MOVES[m] for m in data["moves"]}
    return Pokemon(name, data["level"], data["type"], data["hp"],
                   data["attack"], data["defense"], data["sp_atk"],
                   data["speed"], moves_dict)

# Create two Pokemon
charizard = create_pokemon("Charizard")
blastoise = create_pokemon("Blastoise")

# Start battle
battle = Battle(charizard, blastoise)

print("=== BATTLE START ===")
print(f"Player: {charizard}")
print(f"Enemy: {blastoise}\n")

# Simulate some turns
result = battle.player_attack("Ember")
print(f"Player: {result['message']}")
print(f"Enemy HP: {battle.enemy_pokemon.current_hp}\n")

result = battle.enemy_attack()
print(f"Enemy: {result['message']}")
print(f"Player HP: {battle.player_pokemon.current_hp}\n")

print("Battle status:", battle.get_battle_status()["player"]["hp"], 
      "vs", battle.get_battle_status()["enemy"]["hp"])
```

**Run it**:
```bash
python test_step2.py
```

---

### Step 3: Start Screen
**What to learn**: Pygame Basics, GUI Components, Event Handling

**How to test it**:

Create a test file `test_step3.py`:

```python
import sys
sys.path.insert(0, 'Step_3_Start_Screen')

import pygame
from gui_elements.start_screen import StartScreen

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokemon - Start Screen Test")
clock = pygame.time.Clock()

start_screen = StartScreen()
running = True
selected_team = None

while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            result = start_screen.handle_click(mouse_pos)
            if result == "START_BATTLE":
                selected_team = start_screen.get_selected_team()
                print(f"Team selected: {selected_team}")
                running = False
    
    start_screen.update(mouse_pos)
    start_screen.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(f"Selected team: {selected_team}")
```

**Run it**:
```bash
python test_step3.py
```

---

### Step 4: Complete Battle System
**What to learn**: Full Game Integration, Game Loop, State Management

**How to run it**:

```bash
cd Step_4_Complete_Battle_System
python gui_elements/main_game.py
```

**Controls**:
- **Click Pokemon names** to select 3 for your team
- **Click "Start Battle"** when you have 3 selected
- **Click move buttons** to attack
- **Press R** to return to start screen after battle ends

---

## 🎮 Game Features

### Main Screen
- Select 3 Pokemon from available options
- Each Pokemon has unique stats and moves
- "Start Battle" button activates when 3 are selected

### Battle Screen
- Your Pokemon on the left
- Enemy Pokemon on the right (randomly selected)
- Move buttons (up to 4 per Pokemon)
- Battle log showing what happened
- HP bars for both Pokemon

### Damage Calculation
Based on the Pokemon damage formula:
```
Damage = ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2) 
         × STAB × Type × random
```

---

## 🐛 Troubleshooting

**Q: "ModuleNotFoundError: No module named 'pygame'"**  
A: Install pygame with `pip install pygame`

**Q: "File not found" errors**  
A: Make sure you're running commands from the project root directory

**Q: Buttons not responding**  
A: Make sure you have pygame 2.0+ installed

**Q: Import errors when running tests**  
A: Ensure the sys.path.insert() line in test files points to the correct folder

---

## 📝 Summary Table

| Step | Focus | Run With |
|------|-------|----------|
| 1 | Classes & Dictionaries | `python test_step1.py` |
| 2 | Battle Logic & Formulas | `python test_step2.py` |
| 3 | Pygame & GUI | `python test_step3.py` |
| 4 | Full Game | `python Step_4_Complete_Battle_System/gui_elements/main_game.py` |

---

## 🎯 Next Steps After Completing All 4 Steps

Once your students complete all 4 steps, they can:

1. **Modify move data** - Create new moves or adjust damage values
2. **Add Pokemon** - Extend POKEMON_DATABASE with new creatures
3. **Implement features**:
   - Pokemon switching during battle
   - Status effects (burn, poison)
   - Type-effectiveness in UI
   - Save/load game state
4. **Visual improvements**:
   - Add sprites instead of just names
   - Animated attacks
   - Sound effects

---

Happy learning! 🎓
