# Pokemon Battle Game - Step-by-Step Learning Path

A complete, structured tutorial for teaching Python game development with Pygame, Classes, and Dictionaries.

## 🎮 Project Overview

This project guides students through building a complete **Pokemon turn-based battle game**, progressing from fundamental concepts to a fully playable application.

### What Students Will Learn
- **Classes & Objects**: Creating the Pokemon class with attributes and methods
- **Dictionaries**: Using dictionaries to store moves, stats, and game data
- **Lists**: Managing teams of Pokemon
- **Pygame**: Creating GUI elements and handling events
- **Game Architecture**: Building a complete game with multiple screens
- **Algorithms**: Implementing the Pokemon damage formula
- **Game Design**: Turn-based game logic and state management

---

## 📁 Project Structure

```
Pokemon Game/
├── Step_1_Pokemon_Class_and_Data/
│   ├── pokemon_class/
│   │   └── pokemon.py              # Pokemon class definition
│   ├── gui_elements/               # (empty for now)
│   ├── utilities/
│   │   └── pokemon_data.py          # Pokemon and moves database
│   └── STEP_1_README.md
│
├── Step_2_Battle_Mechanics/
│   ├── pokemon_class/
│   │   └── battle.py               # Battle class and turn logic
│   ├── gui_elements/               # (empty for now)
│   ├── utilities/
│   │   └── damage_calculator.py     # Damage formula implementation
│   └── STEP_2_README.md
│
├── Step_3_Start_Screen/
│   ├── pokemon_class/              # (builds on previous)
│   ├── gui_elements/
│   │   ├── gui_components.py       # Reusable Button, TextDisplay, PokemonCard
│   │   └── start_screen.py         # Pokemon selection screen
│   ├── utilities/                  # (from previous steps)
│   └── STEP_3_README.md
│
├── Step_4_Complete_Battle_System/
│   ├── pokemon_class/
│   │   └── battle_screen.py        # Battle UI and interaction
│   ├── gui_elements/
│   │   ├── battle_screen.py        # Main battle screen
│   │   └── main_game.py            # Game loop and state management
│   ├── utilities/                  # (from previous steps)
│   ├── STEP_4_README.md
│   └── DEPENDENCIES.txt            # Which files to copy from other steps
│
└── README.md (this file)
```

---

## 🚀 Step-by-Step Breakdown

### Step 1: Pokemon Class and Data Structures
**Focus**: Classes, Dictionaries, Data Organization

**What gets built**:
- `Pokemon` class with stats and moves
- Move database (dictionary of moves)
- Pokemon database (dictionary of Pokemon with their data)
- Basic Pokemon methods (take_damage, heal, get_move)

**Key Concepts**:
- Class definition and `__init__` method
- Instance variables and methods
- Dictionaries as databases
- Using dictionaries to store related data

**Learning Time**: ~1-2 hours

---

### Step 2: Battle Mechanics
**Focus**: Game Logic, Mathematical Formulas, Algorithms

**What gets built**:
- `Battle` class for managing turn-based combat
- **Damage Formula Implementation** using the provided equation
- Type effectiveness chart
- Accuracy checking
- Battle state management and logging

**Key Concepts**:
- Turn-based game systems
- Implementing complex mathematical formulas
- Random number generation
- State tracking and transitions

**The Damage Formula**:
```
Damage = ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2) 
         × STAB × Type1 × Type2 × random
```

**Learning Time**: ~2-3 hours

---

### Step 3: Start Screen and GUI
**Focus**: Pygame Basics, Event Handling, UI Design

**What gets built**:
- Reusable `Button` class with hover effects
- `TextDisplay` for rendering text
- `PokemonCard` for displaying Pokemon stats and HP
- `StartScreen` scene where players select 3 Pokemon
- Grid layout for Pokemon selection

**Key Concepts**:
- Pygame rectangles and collision detection
- Rendering text and shapes
- Event handling (mouse clicks)
- UI component design and reusability
- Screen/scene management

**Learning Time**: ~2-3 hours

---

### Step 4: Complete Battle System
**Focus**: Integration, Game Architecture, Application Design

**What gets built**:
- `BattleScreen` with move buttons and battle display
- HP bars and status display
- Turn processing and battle messages
- `PokemonGame` main application class
- Complete game loop
- Scene transitions (Start Screen ↔ Battle)

**Key Concepts**:
- Pygame game loop: events → update → draw
- State management and scene transitions
- Integrating multiple subsystems
- Complete application architecture
- Game flow and user experience

**The Game Flow**:
1. Start Screen: Select 3 Pokemon
2. Battle Screen: Turn-based combat
3. Win/Lose Screen: Return to Start Screen

**Learning Time**: ~2-3 hours

---

## 💻 How to Use This Course Material

### For Teachers
1. **Week 1**: Teach Step 1 in class
   - Introduce classes and dictionaries
   - Have students code along
   - Quiz: "What's the difference between stats and moves?"

2. **Week 2**: Teach Step 2 in class
   - Discuss game loops and state
   - Implement damage formula together
   - Challenge: "Add a burn status effect"

3. **Week 3**: Teach Step 3 in class
   - Introduce pygame basics
   - Build GUI components together
   - Assignment: "Make Pokemon selection prettier"

4. **Week 4**: Teach Step 4 in class
   - Put it all together
   - Debug and optimize
   - Project: "Add features to the game"

### For Students
- Complete one step per week
- Read the README files for context
- Understand the code before modifying it
- Try the extensions and challenges

### Running Each Step

**Step 1**: Test Pokemon class
```python
from pokemon_class.pokemon import Pokemon
from utilities.pokemon_data import POKEMON_DATABASE, MOVES

data = POKEMON_DATABASE["Charizard"]
moves = {name: MOVES[name] for name in data["moves"]}
pokemon = Pokemon(name="Charizard", level=50, pokemon_type=data["type"],
                  hp=data["hp"], attack=data["attack"], defense=data["defense"],
                  sp_atk=data["sp_atk"], speed=data["speed"], moves=moves)
print(pokemon)
```

**Step 2**: Test battle mechanics
```python
from pokemon_class.battle import Battle
# (create two Pokemon objects)
battle = Battle(pokemon1, pokemon2)
result = battle.player_attack("Ember")
print(result["message"])
```

**Step 3**: Run start screen
```python
# Add proper imports and run the StartScreen
# (See STEP_3_README.md for example)
```

**Step 4**: Run complete game
```bash
python Step_4_Complete_Battle_System/gui_elements/main_game.py
```

---

## 📚 Key Concepts by Step

| Concept | Step | Usage |
|---------|------|-------|
| Classes | 1 | Pokemon class |
| Dictionaries | 1 | Moves and Pokemon database |
| Lists | 1 | Move lists, Pokemon team |
| Methods | 1 | take_damage(), heal() |
| Game Logic | 2 | Battle class, turn system |
| Math & Formulas | 2 | Damage calculation |
| Random Numbers | 2 | Critical hits, damage variance |
| Pygame Basics | 3 | Drawing, events, text |
| Collision Detection | 3 | Button clicking |
| Reusable Components | 3 | GUI classes |
| Event Loop | 4 | Game loop pattern |
| State Management | 4 | Screen transitions |
| Integration | 4 | All systems working together |

---

## 🎯 Learning Outcomes

By completing all 4 steps, students will be able to:

✅ Create and use classes with attributes and methods  
✅ Design and use dictionaries for data storage  
✅ Implement complex algorithms and formulas  
✅ Build interactive GUI applications with Pygame  
✅ Design turn-based game systems  
✅ Manage game state and screen transitions  
✅ Debug and extend a complete application  
✅ Understand application architecture and design patterns  

---

## 🔧 Requirements

- Python 3.7+
- Pygame: `pip install pygame`

---

## 💡 Extension Ideas

After completing all 4 steps:

1. **Team Management**
   - Save/load teams
   - Trainer vs Trainer battles
   - Experience and leveling

2. **Enhanced Graphics**
   - Pokemon sprite animations
   - Attack animations
   - Particle effects

3. **Advanced Mechanics**
   - Status effects (burn, poison, paralysis)
   - Weather effects
   - Stat changes (lower attack, raise defense)
   - Abilities and held items

4. **Multiplayer**
   - Local two-player battles
   - Network battles (advanced)
   - Turn timers

5. **Polish**
   - Sound effects and music
   - Main menu
   - Settings screen
   - Pause functionality

---

## 📝 Notes for Instructors

### Teaching Philosophy
- **Progressive Complexity**: Each step builds on previous knowledge
- **Hands-On Learning**: Students code, not just read
- **Practical Application**: Game development teaches real programming
- **Engaging Topic**: Pokemon is relatable to students
- **Extensible**: Built with room for customization

### Common Challenges & Solutions

**Challenge**: Damage values too high/low  
**Solution**: Adjust the formula or change stat values

**Challenge**: Moving between screens not working  
**Solution**: Debug state management in main_game.py

**Challenge**: Buttons not responding to clicks  
**Solution**: Check collision detection and mouse position

**Challenge**: Performance issues  
**Solution**: Reduce FPS cap, optimize draw calls

---

## 📞 Support

- Each step has a detailed README with explanations
- Code is well-commented for student understanding
- Teaching examples provided in each README
- Discussion questions to prompt deeper thinking

---

**Happy Teaching! 🎮**
