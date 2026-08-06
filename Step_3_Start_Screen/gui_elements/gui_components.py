"""
Step 3: GUI Button Component
=============================
A reusable button class for pygame GUI.

Teaching concepts:
- Pygame basics (Rect, Surface)
- Collision detection (mouse over button)
- Object-oriented GUI design
- Reusable components
"""

import pygame
import sys
import os


class Button:
    """A clickable button for the GUI."""
    
    def __init__(self, x, y, width, height, text, color=(100, 100, 100), 
                 text_color=(255, 255, 255), hover_color=(150, 150, 150)):
        """
        Create a button.
        
        Args:
            x, y: Position of button
            width, height: Size of button
            text: Button label
            color: Button color (RGB tuple)
            text_color: Text color (RGB tuple)
            hover_color: Color when mouse hovers over
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hover_color = hover_color
        self.is_hovered = False
        self.is_clicked = False
        
        # Font for button text
        self.font = pygame.font.Font(None, 24)
        
    def draw(self, screen):
        """Draw the button on the screen."""
        # Change color if hovered
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)
        
        # Draw border
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        
        # Draw text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def update(self, mouse_pos):
        """Update button state based on mouse position."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def check_click(self, mouse_pos, mouse_clicked):
        """
        Check if button was clicked.
        
        Args:
            mouse_pos: Current mouse position
            mouse_clicked: True if mouse button pressed
            
        Returns:
            bool: True if button was clicked
        """
        if self.rect.collidepoint(mouse_pos) and mouse_clicked:
            return True
        return False


class TextDisplay:
    """Display text on screen."""
    
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255)):
        """Create a text display."""
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, font_size)
    
    def set_text(self, new_text):
        """Update the displayed text."""
        self.text = new_text
    
    def draw(self, screen):
        """Draw the text on screen."""
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))


class PokemonCard:
    """Display a Pokemon's image and info (simplified)."""
    
    def __init__(self, x, y, pokemon):
        """
        Create a Pokemon card display.
        
        Args:
            x, y: Position on screen
            pokemon: Pokemon object to display
        """
        self.x = x
        self.y = y
        self.pokemon = pokemon
        self.width = 150
        self.height = 200
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.font_large = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 18)
    
    def draw(self, screen):
        """Draw the Pokemon card."""
        # Card background
        pygame.draw.rect(screen, (50, 50, 50), self.rect)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2)
        
        # Pokemon info
        name_text = self.font_large.render(self.pokemon.name, True, (255, 255, 255))
        level_text = self.font_small.render(f"Level: {self.pokemon.level}", True, (200, 200, 200))
        hp_text = self.font_small.render(f"HP: {self.pokemon.current_hp}/{self.pokemon.hp}", True, (100, 255, 100))
        type_text = self.font_small.render(f"Type: {self.pokemon.pokemon_type}", True, (150, 150, 255))
        
        # Blit text to screen
        screen.blit(name_text, (self.x + 10, self.y + 10))
        screen.blit(level_text, (self.x + 10, self.y + 50))
        screen.blit(hp_text, (self.x + 10, self.y + 80))
        screen.blit(type_text, (self.x + 10, self.y + 110))
        
        # HP bar
        bar_width = 130
        bar_height = 15
        hp_ratio = self.pokemon.current_hp / self.pokemon.hp
        
        # Background (red)
        pygame.draw.rect(screen, (200, 0, 0), 
                         (self.x + 10, self.y + 140, bar_width, bar_height))
        
        # Fill (green)
        pygame.draw.rect(screen, (0, 200, 0), 
                         (self.x + 10, self.y + 140, bar_width * hp_ratio, bar_height))
        
        # Border
        pygame.draw.rect(screen, (255, 255, 255), 
                         (self.x + 10, self.y + 140, bar_width, bar_height), 1)
