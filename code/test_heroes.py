""" Tests for hero game mechanics. """
import combat

def test_warrior():
    """ Set of tests to see if the warrior's abilities balance. """
    warrior = combat.combatant(8, 4, 2)
    
    print("Fighting weak monster.")
    victories = 0
    while warrior.health > 0 and victories < 1000:
        monster = combat.combatant(1, 1, 2)
        victories += combat.run_combat(warrior, monster)
    print("Warrior won {} times.".format(victories))
    
    print("Fighting average monster.")
    victories = 0
    while warrior.health > 0 and victories < 1000:
        monster = combat.combatant(2, 1, 2)
        victories += combat.run_combat(warrior, monster)
    print("Warrior won {} times.".format(victories))
    
    print("Fighting strong monster.")
    victories = 0
    while warrior.health > 0 and victories < 1000:
        monster = combat.combatant(3, 1, 2)
        victories += combat.run_combat(warrior, monster)
    print("Warrior won {} times.".format(victories))

def main():
    """ Testing heroes. """
    print("Testing warrior...")
    test_warrior()

if __name__ == '__main__':
    main()
