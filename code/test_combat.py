""" Tests for the combat module."""

import combat

def test_calculate_wounds():
    """ Ensure the calculate_wounds function works properly."""
    attack = [5, 4, 3]
    defense = [2]
    assert combat.calculate_wounds(attack, defense) == 3

    attack = [5, 4, 3]
    defense = []
    assert combat.calculate_wounds(attack, defense) == 3

    attack = []
    defense = [2]
    assert combat.calculate_wounds(attack, defense) == 0

def test_do_attack():
    """ Ensure attack function returns the correct types. """
    assert isinstance(combat.do_attack(3, 5), int)

def test_run_combat():
    """ Ensuring combat works."""

    attacker = combat.combatant(5, 3, 5)
    defender = combat.combatant(5, 3, 5)

    assert isinstance(combat.run_combat(attacker, defender), bool)
