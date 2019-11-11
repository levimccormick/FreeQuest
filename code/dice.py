""" Functions to simulate dice mechanics"""
import random

def compare_lists(attack, defense):
    """compare and discard duplicate values from each list of dice results"""
    for die in attack[:]:
        if die in defense[:]:
            attack.remove(die)
            defense.remove(die)

    return attack, defense

def roll_dice(num):
    """Roll num dice and return a list"""
    results = []
    for _ in range(num):
        results.append(roll_die())

    return results

def roll_die():
    """roll a die"""
    low = 1
    high = 6
    return random.randint(low, high)

if __name__ == '__main__':
    main()
