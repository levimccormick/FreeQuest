""" Tests for game mechanics. """

def test_attack():
    import dice
    damage_total = 0
    attack_dice = 5
    defense_dice = 2
    iterations = 10000
    for _ in range(iterations):
        damage_total += dice.run_attack(attack_dice, defense_dice)

    average_damage = damage_total/iterations
    print('Attack: {} vs Defense: {}'.format(attack_dice, defense_dice))
    print('Average damage: {}'.format(average_damage))

def test_warrior():
    """ Set of tests to see if the warrior's abilities balance. """
