# Step 3: Start Screen and GUI Elements

## Learning Objectives
Students will learn:
- **Pygame Basics**: Drawing shapes, surfaces, and text
- **Event Handling**: Responding to mouse clicks
- **Collision Detection**: Checking if mouse is over a button
- **Layout & Positioning**: Arranging UI elements on screen
- **Reusable Components**: Building GUI elements that can be used throughout the game
- **Screen/Scene Management**: Different screens for different parts of the game

## Files Overview

### `gui_elements/gui_components.py`
Reusable GUI building blocks:
- `Button`: Clickable button with hover effects
  - `draw()`: Render button to screen
  - `update()`: Check if mouse is hovering
  - `check_click()`: Detect if clicked
  
- `TextDisplay`: Simple text renderer
- `PokemonCard`: Display Pokemon stats and HP bar

### `gui_elements/start_screen.py`
The start screen scene:
- Shows all available Pokemon as buttons
- Allows player to select 3 Pokemon for their team
- "Start Battle" button appears after 3 selections
- Returns selected team when ready

## Teaching Example

```python
import pygame
from gui_elements.start_screen import StartScreen

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

start_screen = StartScreen()
selected_team = None

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            result = start_screen.handle_click(mouse_pos)
            if result == "START_BATTLE":
                selected_team = start_screen.get_selected_team()
                print(f"Starting battle with: {selected_team}")
                running = False
    
    start_screen.update(mouse_pos)
    start_screen.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

## Key Pygame Concepts

### Rectangles for Collision Detection
```python
button_rect = pygame.Rect(x, y, width, height)
if button_rect.collidepoint(mouse_x, mouse_y):
    print("Mouse is over button!")
```

### Rendering Text
```python
font = pygame.font.Font(None, 24)  # None = default font, 24 = size
text_surface = font.render("Hello", True, (255, 255, 255))
screen.blit(text_surface, (x, y))
```

### Drawing Shapes
```python
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, w, h))  # Filled
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, w, h), 2)  # Border
```

## GUI Design Principles Discussed

1. **Visual Feedback**: Buttons change color on hover
2. **Clear Status**: Display how many Pokemon are selected
3. **Progressive Disclosure**: Start button only appears when ready
4. **Layout**: Organize Pokemon buttons in a grid
5. **Consistency**: All buttons use the same style

## Discussion Questions

- Why separate GUI components into different classes?
- How would we disable buttons that have already been selected?
- Could we show preview images of each Pokemon?
- How might we animate button clicks?

## Extensions

- Add Pokemon type colors (Fire = red, Water = blue, etc.)
- Display move previews for selected Pokemon
- Add a "random team" button
- Animated Pokemon sprites instead of just names
