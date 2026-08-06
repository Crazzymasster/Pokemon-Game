"""
Step 2: Battle System
=====================
This module contains the core battle logic:
- Turn-based battle system
- Move selection and execution
- Battle status management

Teaching concepts:
- Game loops and turn systems
- State management
- Error handling
"""


class Battle:
    """Manages a turn-based Pokemon battle."""
    
    def __init__(self, player_pokemon, enemy_pokemon):
        """
        Initialize a battle between two Pokemon.
        
        Args:
            player_pokemon (Pokemon): The player's active Pokemon
            enemy_pokemon (Pokemon): The enemy's active Pokemon
        """
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.turn_count = 0
        self.battle_log = []  # Record of battle events
        self.is_active = True
        
    def player_attack(self, move_name):
        """
        Execute a player's attack with a specific move.
        
        Args:
            move_name (str): Name of the move to use
            
        Returns:
            dict: Battle result with damage and status
        """
        if not self.player_pokemon.is_alive():
            return {"success": False, "message": "Your Pokemon is fainted!"}
        
        if not self.enemy_pokemon.is_alive():
            return {"success": False, "message": "Battle is over!"}
        
        move = self.player_pokemon.get_move(move_name)
        if not move:
            return {"success": False, "message": f"{move_name} not found!"}
        
        # Calculate damage and apply it
        damage = self.calculate_damage(self.player_pokemon, self.enemy_pokemon, move)
        self.enemy_pokemon.take_damage(damage)
        
        message = f"{self.player_pokemon.name} used {move_name}! Dealt {damage} damage!"
        self.battle_log.append(message)
        
        return {
            "success": True,
            "attacker": self.player_pokemon.name,
            "move": move_name,
            "damage": damage,
            "defender_hp": self.enemy_pokemon.current_hp,
            "message": message
        }
    
    def enemy_attack(self):
        """
        Enemy selects a random move and attacks.
        
        Returns:
            dict: Battle result with damage and status
        """
        if not self.enemy_pokemon.is_alive():
            return {"success": False, "message": "Battle is over!"}
        
        import random
        moves = self.enemy_pokemon.get_all_moves()
        random_move = random.choice(moves)
        move = self.enemy_pokemon.get_move(random_move)
        
        damage = self.calculate_damage(self.enemy_pokemon, self.player_pokemon, move)
        self.player_pokemon.take_damage(damage)
        
        message = f"{self.enemy_pokemon.name} used {random_move}! Dealt {damage} damage!"
        self.battle_log.append(message)
        
        return {
            "success": True,
            "attacker": self.enemy_pokemon.name,
            "move": random_move,
            "damage": damage,
            "defender_hp": self.player_pokemon.current_hp,
            "message": message
        }
    
    def calculate_damage(self, attacker, defender, move):
        """
        Calculate damage using the Pokemon damage formula.
        
        Formula: ((2 × Level ÷ 5 + 2) × Power × A/D / 50 + 2) × STAB × Type1 × Type2 × random
        
        Args:
            attacker (Pokemon): The attacking Pokemon
            defender (Pokemon): The defending Pokemon
            move (dict): The move being used
            
        Returns:
            int: Calculated damage value
        """
        from utilities.damage_calculator import calculate_pokemon_damage
        return calculate_pokemon_damage(attacker, defender, move)
    
    def get_battle_status(self):
        """Return current battle status."""
        return {
            "turn": self.turn_count,
            "player": {
                "name": self.player_pokemon.name,
                "hp": self.player_pokemon.current_hp,
                "max_hp": self.player_pokemon.hp,
                "level": self.player_pokemon.level,
                "alive": self.player_pokemon.is_alive()
            },
            "enemy": {
                "name": self.enemy_pokemon.name,
                "hp": self.enemy_pokemon.current_hp,
                "max_hp": self.enemy_pokemon.hp,
                "level": self.enemy_pokemon.level,
                "alive": self.enemy_pokemon.is_alive()
            },
            "is_active": self.is_active
        }
    
    def check_battle_end(self):
        """Check if the battle is over."""
        if not self.player_pokemon.is_alive():
            self.is_active = False
            self.battle_log.append(f"{self.player_pokemon.name} fainted! You lost!")
            return True
        
        if not self.enemy_pokemon.is_alive():
            self.is_active = False
            self.battle_log.append(f"{self.enemy_pokemon.name} fainted! You won!")
            return True
        
        return False
    
    def get_battle_log(self):
        """Return the list of battle events."""
        return self.battle_log
