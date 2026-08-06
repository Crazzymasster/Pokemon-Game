"""
Step 4: Battle Class (copied from Step 2)
"""


class Battle:
    """Manages a turn-based Pokemon battle."""
    
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.turn_count = 0
        self.battle_log = []
        self.is_active = True
        
    def player_attack(self, move_name):
        if not self.player_pokemon.is_alive():
            return {"success": False, "message": "Your Pokemon is fainted!"}
        
        if not self.enemy_pokemon.is_alive():
            return {"success": False, "message": "Battle is over!"}
        
        move = self.player_pokemon.get_move(move_name)
        if not move:
            return {"success": False, "message": f"{move_name} not found!"}
        
        damage = self.calculate_damage(self.player_pokemon, self.enemy_pokemon, move)
        self.enemy_pokemon.take_damage(damage)
        
        message = f"{self.player_pokemon.name} used {move_name}! Dealt {damage} damage!"
        
        # Check type effectiveness by recalculating
        from utilities.damage_calculator import get_type_effectiveness
        type_effectiveness = get_type_effectiveness(move.get("type"), self.enemy_pokemon.pokemon_type)
        if type_effectiveness > 1.0:
            message += " It's super effective!"
        elif type_effectiveness < 1.0:
            message += " It's not very effective..."
        
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
        if not self.enemy_pokemon.is_alive():
            return {"success": False, "message": "Battle is over!"}
        
        import random
        moves = self.enemy_pokemon.get_all_moves()
        random_move = random.choice(moves)
        move = self.enemy_pokemon.get_move(random_move)
        
        damage = self.calculate_damage(self.enemy_pokemon, self.player_pokemon, move)
        self.player_pokemon.take_damage(damage)
        
        message = f"{self.enemy_pokemon.name} used {random_move}! Dealt {damage} damage!"
        
        # Check type effectiveness by recalculating
        from utilities.damage_calculator import get_type_effectiveness
        type_effectiveness = get_type_effectiveness(move.get("type"), self.player_pokemon.pokemon_type)
        if type_effectiveness > 1.0:
            message += " It's super effective!"
        elif type_effectiveness < 1.0:
            message += " It's not very effective..."
        
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
        from utilities.damage_calculator import calculate_pokemon_damage
        damage, type_effectiveness = calculate_pokemon_damage(attacker, defender, move)
        return damage
    
    def get_battle_status(self):
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
        return self.battle_log
