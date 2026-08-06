# Step 4: Complete Battle System - Full Game

## Learning Objectives
Students will learn:
- **Game Loop**: The classic pygame event loop pattern
- **State Management**: Switching between different screens/scenes
- **Integration**: Bringing together all previous components
- **Data Flow**: How data flows from selection through to battle
- **Object Lifecycle**: Creating and managing multiple objects
- **Complete Application Architecture**: Full game structure

## Files Overview

### `gui_elements/battle_screen.py`
The battle interface:
- Displays both Pokemon with HP bars
- Shows 4 move buttons
- Displays battle messages
- Shows current team status
- Manages turn execution
- Displays win/lose screen

### `gui_elements/main_game.py`
The main game application:
- `PokemonGame`: Main class managing game state
- Game loop: events → update → draw
- Scene management: START_SCREEN ↔ BATTLE
- Pokemon creation from database
- Event handling
- `main()`: Entry point

## Game Flow

```
1. User starts game
2. StartScreen displays all Pokemon
3. User clicks 3 Pokemon to select team
4. User clicks "Start Battle"
5. Random enemy Pokemon is chosen
6. BattleScreen displays:
   - Player Pokemon (left)
   - Enemy Pokemon (right)
   - Move buttons
7. User clicks a move
8. Player attacks → Damage calculated
9. Check if enemy fainted
10. Enemy attacks → Damage calculated
11. Check if player fainted
12. Repeat until someone loses
13. Display winner
14. Press R to return to start screen
```

## Teaching Example

```python
from gui_elements.main_game import PokemonGame

# Create and run the game
game = PokemonGame(width=800, height=600, fps=60)
game.run()
```

## The Pygame Game Loop

### Classic Structure:
```python
while game_running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    # 2. Update Game Logic
    player.update()
    enemy.update()
    
    # 3. Draw Everything
    screen.fill((0, 0, 0))
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)  # 60 FPS
```

## Key Architecture Decisions

1. **Separation of Concerns**:
   - StartScreen handles selection UI
   - BattleScreen handles battle UI
   - Battle class handles game logic
   - Main game coordinates everything

2. **Object Composition**:
   - BattleScreen contains Pokemon objects
   - BattleScreen contains Battle object
   - PokemonGame contains StartScreen and BattleScreen

3. **Event Flow**:
   - User clicks button
   - main_game detects click
   - main_game calls appropriate screen/battle method
   - Screen updates and returns result
   - main_game updates state

## State Diagram

```
        ┌─────────────────┐
        │  START_SCREEN   │
        └────────┬────────┘
                 │ "START_BATTLE" event
                 ↓
        ┌─────────────────┐
        │     BATTLE      │
        └────────┬────────┘
                 │ Press R or Battle ends
                 ↓
        ┌─────────────────┐
        │  START_SCREEN   │ (reset)
        └─────────────────┘
```

## Discussion Questions

- Why separate StartScreen and BattleScreen into different classes?
- How does the game know which screen to update/draw?
- What happens if the player's Pokemon all faint?
- Could we add a third screen for results/stats?

## Extensions for Students

- Add a Pokemon switch menu during battle
- Implement a turn counter
- Add sound effects for moves
- Display move descriptions on hover
- Add type effectiveness indicator
- Implement a replay system
- Add experience/leveling after battle
- Create a Pokemon storage/box system

## Running the Game

```bash
python gui_elements/main_game.py
```

Requirements:
- pygame library: `pip install pygame`
