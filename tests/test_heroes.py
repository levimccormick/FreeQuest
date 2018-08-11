""" Tests for hero game mechanics. """
import combat

def test_warrior():
    """ Set of tests to see if the warrior's abilities balance. """
    warrior = combat.combatant(8, 4, 2)

    victories = 0
    while warrior.health > 0 and victories < 1000:
        weak_monster = combat.combatant(1, 1, 2)
        victories += combat.run_combat(warrior, weak_monster)

    print("Warrior won {} times.".format(victories))
