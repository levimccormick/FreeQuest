def main():
    damageTotal = 0
    attackDice = 5
    defenseDice = 2
    iterations = 10000
    for x in range(iterations):
        damageTotal += runAttack(attackDice,defenseDice)
        
    averageDamage = damageTotal/iterations
    print('Attack: {} vs Defense: {}'.format(attackDice,defenseDice))
    print('Average damage: {}'.format(averageDamage))

def runAttack(attackDice,defenseDice):
    # simulate an attack between two values
    attack = rollDice(attackDice)
    defense = rollDice(defenseDice)
    attack,defense = compareLists(attack,defense)
    damage = calculateDamage(attack,defense)
    return damage

def calculateDamage(attack,defense):
    damage = 0
    if not defense:
        target = 0
    else:
        target = max(defense)

    for x in attack[:]:
        if x >= target:
            damage += x

    return damage

def calculateWounds(attack,defense):
    wounds = 0
    if not defense:
        target = 0
    else:
        target = max(defense)

    for x in attack[:]:
        if x >= target:
            wounds += 1

    return wounds

def compareLists(attack,defense):
    # compare and discard duplicate values from each list of dice results
    for x in attack[:]:
        if x in defense[:]:
            attack.remove(x)
            defense.remove(x)

    return attack,defense

def rollDice(num):
    # Roll num dice and return a list
    results = []
    for _ in range(num):
        results.append(rollDie())

    return results

def rollDie():
    import random
    # roll a die
    min = 1
    max = 6
    return random.randint(min,max)



if __name__ == '__main__':
    main()
