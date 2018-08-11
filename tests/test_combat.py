""" Tests for the combat module."""

from freequest import combat


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

# def test_attack_values():
#     """ Test various attack vs defense values. """
#     from tabulate import tabulate
#     iterations = 10000
#     table = []
#     for defense in range(1, 11):
#         row = [defense]
#         for attack in range(1, 11):
#             wounds = 0
#             for _ in range(iterations):
#                 wounds += combat.do_attack(attack, defense)
#             row.append(float(wounds)/iterations)
#
#         table.append(row)
#     print "Defense vs Attack values:"
#     print tabulate(table, headers=['Defense', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
