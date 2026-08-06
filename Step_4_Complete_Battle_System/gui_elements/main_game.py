"""
Step 4: Main Game Application
=============================
The main game loop that ties everything together.

Teaching concepts:
- Pygame game loop (events, update, draw)
- Scene/state management
- Integration of all previous components
- Event handling
"""

import sys
import os

# Add Step_4 root to path so we can import from packages
_current_file = os.path.abspath(__file__)
_gui_dir = os.path.dirname(_current_file)  # Step_4_Complete_Battle_System/gui_elements
_step4_root = os.path.dirname(_gui_dir)     # Step_4_Complete_Battle_System
if _step4_root not in sys.path:
    sys.path.insert(0, _step4_root)

import pygame
from gui_elements.start_screen import StartScreen
from gui_elements.battle_screen import BattleScreen
from pokemon_class.pokemon import Pokemon
from utilities.pokemon_data import POKEMON_DATABASE, MOVES, get_random_pokemon


class PokemonGame:
    """Main game application."""
    
    def __init__(self, width=1000, height=700, fps=60):
        """
        Initialize the game.
        
        Args:
            width: Screen width
            height: Screen height
            fps: Frames per second
        """
        pygame.init()
        
        self.width = width
        self.height = height
        self.fullscreen = False
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("Pokemon Battle Game")
        
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        
        # Game states
        self.current_state = "START_SCREEN"
        self.start_screen = StartScreen(width, height)
        self.battle_screen = None
    
    def create_pokemon_from_data(self, pokemon_name):
        """
        Create a Pokemon instance from database data.
        
        Args:
            pokemon_name: Name of Pokemon to create
            
        Returns:
            Pokemon: Initialized Pokemon object
        """
        data = POKEMON_DATABASE[pokemon_name]
        
        # Convert move names to move dictionaries
        pokemon_moves = {}
        for move_name in data["moves"]:
            if move_name in MOVES:
                pokemon_moves[move_name] = MOVES[move_name]
        
        # Create Pokemon
        return Pokemon(
            name=pokemon_name,
            level=data["level"],
            pokemon_type=data["type"],
            hp=data["hp"],
            attack=data["attack"],
            defense=data["defense"],
            sp_atk=data["sp_atk"],
            speed=data["speed"],
            moves=pokemon_moves
        )
    
    def start_battle(self, player_team_names):
        """
        Initialize a new battle.
        
        Args:
            player_team_names: List of 3 Pokemon names
        """
        # Create player's team
        player_team = [self.create_pokemon_from_data(name) 
                      for name in player_team_names]
        
        # Create random enemy Pokemon
        enemy_name = get_random_pokemon()
        enemy_pokemon = self.create_pokemon_from_data(enemy_name)
        
        # Create battle screen
        self.battle_screen = BattleScreen(player_team, enemy_pokemon, self.width, self.height)
        self.current_state = "BATTLE"
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resize
                self.width, self.height = event.size
                if not self.fullscreen:
                    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                # Update screen dimensions in both screens
                self.start_screen.resize(self.width, self.height)
                if self.battle_screen:
                    self.battle_screen.resize(self.width, self.height)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if self.current_state == "START_SCREEN":
                    result = self.start_screen.handle_click(mouse_pos)
                    if result == "START_BATTLE":
                        self.start_battle(self.start_screen.get_selected_team())
                
                elif self.current_state == "BATTLE":
                    move_selected = self.battle_screen.handle_move_selection(mouse_pos)
                    if move_selected:
                        self.battle_screen.process_turn(move_selected)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.current_state == "BATTLE":
                        # Return to start screen
                        self.current_state = "START_SCREEN"
                        self.start_screen.reset()
                
                elif event.key == pygame.K_f:
                    # Toggle fullscreen
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
    
    def update(self):
        """Update game logic."""
        mouse_pos = pygame.mouse.get_pos()
        
        if self.current_state == "START_SCREEN":
            self.start_screen.update(mouse_pos)
        
        elif self.current_state == "BATTLE":
            self.battle_screen.update(mouse_pos)
    
    def draw(self):
        """Draw all game elements."""
        if self.current_state == "START_SCREEN":
            self.start_screen.draw(self.screen)
        
        elif self.current_state == "BATTLE":
            self.battle_screen.draw(self.screen)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    game = PokemonGame()
    game.run()


if __name__ == "__main__":
    main()
