"""
Step 3: Pokemon Class (copied from Step 1)
This file should be here so Step 3 is self-contained.
"""


class Pokemon:
    """A Pokemon with stats and moves."""
    
    def __init__(self, name, level, pokemon_type, hp, attack, defense, sp_atk, speed, moves):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.speed = speed
        self.current_hp = hp
        self.moves = moves
        
    def is_alive(self):
        return self.current_hp > 0
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.hp:
            self.current_hp = self.hp
    
    def get_move(self, move_name):
        if move_name in self.moves:
            return self.moves[move_name]
        return None
    
    def get_all_moves(self):
        return list(self.moves.keys())
    
    def __str__(self):
        hp_bar = f"{self.current_hp}/{self.hp}"
        return f"{self.name} (Lvl. {self.level}) - {hp_bar} HP"
