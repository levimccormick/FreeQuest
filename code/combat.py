""" Functions to simulate combat resolution."""
import dice

class combatant:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

def do_attack(attack_dice, defense_dice):
    """Simulate the dice mechanics of the combat system."""
    
    # Generate the dice rolls of the two combatants
    attack = dice.roll_dice(attack_dice)
    defense = dice.roll_dice(defense_dice)
    # Compare the dice lists, discarding duplicates
    attack, defense = dice.compare_lists(attack, defense)
    # Calculate how much damage is done by the attack.
    damage = calculate_wounds(attack, defense)
    return damage

def calculate_wounds(attack=[0], defense=[0]):
    """ Determine wounds from two dice lists.
    
        Damage equals the count of attack dice greater than or equal to the highest
            defense roll.
    """
    if not defense:
        defense = [0]
        
    return sum(value >= max(defense) for value in attack)

def run_combat(attacker, defender):
    """ Simulate simple combat between two opponents."""

    while attacker.health > 0 and defender.health > 0:
        # Attacker attacks defender
        if attacker.health > 0:
            defender.health = defender.health - do_attack(attacker.attack, defender.defense)
        # Defender counter attacks
        if defender.health > 0:
            attacker.health = attacker.health - do_attack(defender.attack, attacker.defense)
    # If the attacker's health is > 0, the defender died first
    return attacker.health > 0
