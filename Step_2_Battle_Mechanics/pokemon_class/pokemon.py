"""
Step 2: Pokemon Class (copied from Step 1)
This file should be here so Step 2 is self-contained.
"""


class Pokemon:
    """A Pokemon with stats and moves."""
    
    def __init__(self, name, level, pokemon_type, hp, attack, defense, sp_atk, speed, moves):
        """
        Initialize a Pokemon.
        
        Args:
            name (str): Pokemon's name
            level (int): Pokemon's level
            pokemon_type (str): Pokemon's type (fire, water, grass, normal, etc.)
            hp (int): Base HP stat
            attack (int): Attack stat
            defense (int): Defense stat
            sp_atk (int): Special Attack stat
            speed (int): Speed stat
            moves (dict): Dictionary of moves - {move_name: {power, accuracy, type}}
        """
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        
        # Stats
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.speed = speed
        
        # Current HP (changes during battle)
        self.current_hp = hp
        
        # Moves dictionary - stores move info
        self.moves = moves
        
    def is_alive(self):
        """Check if the Pokemon is still in battle."""
        return self.current_hp > 0
    
    def take_damage(self, damage):
        """Reduce current HP by damage amount."""
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def heal(self, amount):
        """Restore HP (up to max)."""
        self.current_hp += amount
        if self.current_hp > self.hp:
            self.current_hp = self.hp
    
    def get_move(self, move_name):
        """Get move details by name."""
        if move_name in self.moves:
            return self.moves[move_name]
        return None
    
    def get_all_moves(self):
        """Return list of all move names."""
        return list(self.moves.keys())
    
    def __str__(self):
        """String representation of Pokemon."""
        hp_bar = f"{self.current_hp}/{self.hp}"
        return f"{self.name} (Lvl. {self.level}) - {hp_bar} HP"
