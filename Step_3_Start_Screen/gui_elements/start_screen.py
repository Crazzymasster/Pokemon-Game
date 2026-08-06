"""
Step 3: Start Screen Scene
===========================
The opening screen where players select their 3 Pokemon.

Teaching concepts:
- Screen/Scene management
- Event handling (mouse clicks)
- Layout and positioning
- Lists and iteration
"""

import pygame
import sys
import os

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from gui_elements.gui_components import Button, TextDisplay, PokemonCard
from utilities.pokemon_data import POKEMON_DATABASE


class StartScreen:
    """The Pokemon selection screen."""
    
    def __init__(self, screen_width=800, screen_height=600):
        """
        Initialize the start screen.
        
        Args:
            screen_width: Screen width in pixels
            screen_height: Screen height in pixels
        """
        self.width = screen_width
        self.height = screen_height
        
        # Title
        self.title = TextDisplay(20, 20, "Choose Your Pokemon Team!", font_size=36)
        
        # Available Pokemon to select from
        self.available_pokemon = list(POKEMON_DATABASE.keys())
        self.selected_pokemon = []  # Will store 3 selected Pokemon
        
        # Create buttons for each available Pokemon
        self.pokemon_buttons = []
        self._create_pokemon_buttons()
        
        # Info display
        self.info_text = TextDisplay(20, 500, f"Selected: {len(self.selected_pokemon)}/3", 
                                     font_size=20)
        
        # Start battle button (appears when 3 Pokemon selected)
        self.start_button = Button(650, 520, 120, 50, "Start Battle", 
                                   color=(0, 200, 0), hover_color=(0, 255, 0))
        self.start_button_active = False
    
    def _create_pokemon_buttons(self):
        """Create buttons for selecting each Pokemon."""
        button_width = 150
        button_height = 40
        buttons_per_row = 4
        start_x = 20
        start_y = 80
        spacing = 15
        
        for i, pokemon_name in enumerate(self.available_pokemon):
            row = i // buttons_per_row
            col = i % buttons_per_row
            
            x = start_x + col * (button_width + spacing)
            y = start_y + row * (button_height + spacing)
            
            button = Button(x, y, button_width, button_height, pokemon_name,
                           color=(100, 100, 150), hover_color=(150, 150, 200))
            self.pokemon_buttons.append((pokemon_name, button))
    
    def handle_click(self, mouse_pos):
        """
        Handle mouse clicks on Pokemon selection buttons.
        
        Args:
            mouse_pos: (x, y) position of mouse click
        """
        # Check if Pokemon buttons were clicked
        for pokemon_name, button in self.pokemon_buttons:
            if button.check_click(mouse_pos, True):
                if len(self.selected_pokemon) < 3:
                    self.selected_pokemon.append(pokemon_name)
                    self.info_text.set_text(f"Selected: {len(self.selected_pokemon)}/3 - {pokemon_name}")
                    
                    # Update button states (could show selected Pokemon differently)
                    if len(self.selected_pokemon) >= 3:
                        self.start_button_active = True
        
        # Check if start button was clicked
        if self.start_button_active and self.start_button.check_click(mouse_pos, True):
            return "START_BATTLE"
        
        return None
    
    def update(self, mouse_pos):
        """
        Update screen state (e.g., button hover effects).
        
        Args:
            mouse_pos: Current mouse position
        """
        for pokemon_name, button in self.pokemon_buttons:
            button.update(mouse_pos)
        
        if self.start_button_active:
            self.start_button.update(mouse_pos)
    
    def draw(self, screen):
        """
        Draw the entire start screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Clear screen
        screen.fill((30, 30, 30))
        
        # Draw title
        self.title.draw(screen)
        
        # Draw Pokemon selection buttons
        for pokemon_name, button in self.pokemon_buttons:
            button.draw(screen)
        
        # Draw selected Pokemon
        if self.selected_pokemon:
            display_text = "Selected Team: " + ", ".join(self.selected_pokemon)
            selected_display = TextDisplay(20, 450, display_text, font_size=18, 
                                          color=(200, 200, 100))
            selected_display.draw(screen)
        
        # Draw info text
        self.info_text.draw(screen)
        
        # Draw start button if 3 Pokemon selected
        if self.start_button_active:
            self.start_button.draw(screen)
    
    def get_selected_team(self):
        """Return the list of selected Pokemon names."""
        return self.selected_pokemon.copy()
    
    def reset(self):
        """Reset the screen for a new selection."""
        self.selected_pokemon = []
        self.start_button_active = False
        self.info_text.set_text("Selected: 0/3")
