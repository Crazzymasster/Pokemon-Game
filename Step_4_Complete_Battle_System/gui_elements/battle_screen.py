"""
Step 4: Battle Screen
=====================
The main battle interface where combat takes place.

Teaching concepts:
- Integrating all previous components
- Managing multiple UI elements
- Turn management and state transitions
- User feedback and responsiveness
"""

import pygame
from gui_elements.gui_components import Button, TextDisplay, PokemonCard
from pokemon_class.battle import Battle


class BattleScreen:
    """Main battle screen with UI for combat."""
    
    def __init__(self, player_team, enemy_pokemon, screen_width=1000, screen_height=700):
        """
        Initialize the battle screen.
        
        Args:
            player_team: List of player's Pokemon objects
            enemy_pokemon: Enemy Pokemon object
            screen_width: Screen width in pixels
            screen_height: Screen height in pixels
        """
        self.player_team = player_team
        self.current_player_index = 0
        self.current_player_pokemon = player_team[0]
        
        self.enemy_pokemon = enemy_pokemon
        
        # Screen dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Initialize battle
        self.battle = Battle(self.current_player_pokemon, self.enemy_pokemon)
        
        # Game state (must be before _create_ui)
        self.waiting_for_move = True
        self.last_battle_message = "Choose a move!"
        self.battle_over = False
        self.winner = None
        self.showing_moves = True  # Track whether showing moves or results
        
        # UI Elements
        self._create_ui()
    
    def _create_ui(self):
        """Create all UI elements for the battle screen."""
        # Pokemon cards - classic Pokemon battle layout
        # Enemy card at top (center-right area)
        enemy_x = int(self.screen_width * 0.55)
        enemy_y = int(self.screen_height * 0.08)
        self.enemy_card = PokemonCard(enemy_x, enemy_y, self.enemy_pokemon)
        
        # Player card at bottom (left side)
        player_x = int(self.screen_width * 0.08)
        player_y = int(self.screen_height * 0.68)
        self.player_card = PokemonCard(player_x, player_y, self.current_player_pokemon)
        
        # Battle message display - middle area
        msg_x = int(self.screen_width * 0.05)
        msg_y = int(self.screen_height * 0.38)
        self.message_display = TextDisplay(msg_x, msg_y, self.last_battle_message, 
                                          font_size=14)
        
        # Action box at bottom - contains either moves or battle results
        self.action_box_x = int(self.screen_width * 0.05)
        self.action_box_y = int(self.screen_height * 0.73)
        self.action_box_width = int(self.screen_width * 0.9)
        self.action_box_height = int(self.screen_height * 0.22)
        self.action_box_rect = pygame.Rect(self.action_box_x, self.action_box_y, 
                                           self.action_box_width, self.action_box_height)
        
        # Move buttons - 2x2 grid inside action box
        move_names = self.current_player_pokemon.get_all_moves()
        self.move_buttons = []
        
        # Scale button size to fit inside action box
        button_width = int(self.action_box_width * 0.42)
        button_height = int(self.action_box_height * 0.42)
        
        # Grid layout inside box: 2 columns, 2 rows
        start_x = int(self.action_box_x + self.action_box_width * 0.04)
        start_y = int(self.action_box_y + self.action_box_height * 0.08)
        spacing_x = int(self.action_box_width * 0.04)
        spacing_y = int(self.action_box_height * 0.08)
        
        for i, move_name in enumerate(move_names[:4]):  # Limit to 4 moves
            col = i % 2
            row = i // 2
            x = start_x + col * (button_width + spacing_x)
            y = start_y + row * (button_height + spacing_y)
            
            button = Button(x, y, button_width, button_height, move_name,
                           color=(50, 100, 150), hover_color=(100, 150, 200))
            self.move_buttons.append((move_name, button))
        
        # Team status - show all 3 Pokemon in team at top
        team_x = int(self.screen_width * 0.02)
        team_y = int(self.screen_height * 0.01)
        team_text = " | ".join([f"{p.name} ({p.current_hp}/{p.hp})" 
                                for p in self.player_team])
        self.team_display = TextDisplay(team_x, team_y, f"Team: {team_text}", font_size=12)
    
    def resize(self, new_width, new_height):
        """
        Resize all UI elements to fit new screen dimensions.
        
        Args:
            new_width: New screen width
            new_height: New screen height
        """
        self.screen_width = new_width
        self.screen_height = new_height
        self._create_ui()
    
    def handle_move_selection(self, mouse_pos):
        """
        Handle player selecting a move or clicking to continue from results.
        
        Args:
            mouse_pos: (x, y) position of mouse click
            
        Returns:
            str: The move name if selected, None otherwise
        """
        # If showing results, check if action box was clicked to return to moves
        if not self.showing_moves:
            if self.action_box_rect.collidepoint(mouse_pos):
                self.showing_moves = True
                self.waiting_for_move = True
            return None
        
        # If showing moves, check for move button clicks
        for move_name, button in self.move_buttons:
            if button.check_click(mouse_pos, True):
                return move_name
        return None
    
    def process_turn(self, player_move):
        """
        Execute a complete turn (player move + enemy response).
        
        Args:
            player_move: Name of move the player selected
        """
        if not self.waiting_for_move:
            return  # Still processing previous turn
        
        self.waiting_for_move = False
        
        # Player attacks
        attack_result = self.battle.player_attack(player_move)
        if attack_result["success"]:
            self.last_battle_message = attack_result["message"]
        else:
            self.last_battle_message = attack_result["message"]
            self.waiting_for_move = True
            return
        
        # Check if battle is over after player attack
        if self.battle.check_battle_end():
            self.battle_over = True
            self.winner = "PLAYER"
            self.last_battle_message = "You won the battle!"
            self.waiting_for_move = True
            return
        
        # Enemy attacks
        enemy_result = self.battle.enemy_attack()
        self.last_battle_message = f"{self.last_battle_message}\n{enemy_result['message']}"
        
        # Check if battle is over after enemy attack
        if self.battle.check_battle_end():
            self.battle_over = True
            self.winner = "ENEMY"
            self.last_battle_message = f"{self.last_battle_message}\nYou lost!"
            self.waiting_for_move = True
            return
        
        # Update card displays
        self._update_ui()
        
        self.waiting_for_move = True
        self.showing_moves = False  # Show battle results in action box
    
    def _update_ui(self):
        """Refresh UI elements with current battle state."""
        # Use responsive positioning consistent with _create_ui
        enemy_x = int(self.screen_width * 0.55)
        enemy_y = int(self.screen_height * 0.08)
        player_x = int(self.screen_width * 0.08)
        player_y = int(self.screen_height * 0.68)
        
        self.player_card = PokemonCard(player_x, player_y, self.current_player_pokemon)
        self.enemy_card = PokemonCard(enemy_x, enemy_y, self.enemy_pokemon)
        
        # Update message display
        self.message_display.set_text(self.last_battle_message)
        
        # Update team display
        team_text = " | ".join([f"{p.name} ({p.current_hp}/{p.hp})" 
                                for p in self.player_team])
        self.team_display.set_text(f"Team: {team_text}")
    
    def switch_pokemon(self, new_index):
        """
        Switch to a different Pokemon.
        
        Args:
            new_index: Index of new Pokemon in player_team
        """
        if 0 <= new_index < len(self.player_team):
            if self.player_team[new_index].is_alive():
                self.current_player_index = new_index
                self.current_player_pokemon = self.player_team[new_index]
                self.battle.player_pokemon = self.current_player_pokemon
                self.last_battle_message = f"Go, {self.current_player_pokemon.name}!"
                self._update_ui()
    
    def update(self, mouse_pos):
        """
        Update button hover states.
        
        Args:
            mouse_pos: Current mouse position
        """
        for move_name, button in self.move_buttons:
            button.update(mouse_pos)
    
    def draw(self, screen):
        """
        Draw the entire battle screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Clear screen
        screen.fill((20, 20, 40))
        
        # Draw Pokemon cards
        self.player_card.draw(screen)
        self.enemy_card.draw(screen)
        
        # Draw action box (border)
        pygame.draw.rect(screen, (100, 100, 100), self.action_box_rect, 2)
        
        # Draw moves or results inside action box
        if self.showing_moves and not self.battle_over:
            # Draw move buttons inside the action box
            for move_name, button in self.move_buttons:
                button.draw(screen)
        else:
            # Draw battle results text inside the action box
            result_y = int(self.action_box_y + self.action_box_height * 0.2)
            result_display = TextDisplay(int(self.action_box_x + self.action_box_width * 0.05), 
                                        result_y, self.last_battle_message, font_size=14)
            result_display.draw(screen)
            
            # Add instruction text
            instruction_y = int(self.action_box_y + self.action_box_height * 0.65)
            instruction = TextDisplay(int(self.action_box_x + self.action_box_width * 0.05), 
                                     instruction_y, "Click to continue...", font_size=12,
                                     color=(200, 200, 200))
            instruction.draw(screen)
        
        # Draw message (above action box)
        self.message_display.draw(screen)
        
        # Draw team status
        self.team_display.draw(screen)
        
        # If battle is over, show result
        if self.battle_over:
            result_text = "VICTORY!" if self.winner == "PLAYER" else "DEFEAT!"
            result_color = (0, 255, 0) if self.winner == "PLAYER" else (255, 0, 0)
            result_display = TextDisplay(350, 250, result_text, font_size=48, 
                                        color=result_color)
            result_display.draw(screen)
            
            # Draw restart button
            restart_text = TextDisplay(300, 350, "Press R to return to menu", 
                                      font_size=20)
            restart_text.draw(screen)
    
    def get_game_state(self):
        """Return current game state."""
        return {
            "battle_active": not self.battle_over,
            "player_alive": self.current_player_pokemon.is_alive(),
            "enemy_alive": self.enemy_pokemon.is_alive(),
            "winner": self.winner,
            "last_message": self.last_battle_message
        }
