import dice

# def main():
#     iterations = 100000
#     for item in [(2,2),(5,4),(6,8)]:
#         hits = 0
#         damageTotal = 0
#         for _ in range(iterations):
#             damage = dice.runAttack(item[0],item[1])
#             if damage > 0:
#                 hits += 1
#                 damageTotal += damage
#
#         print('{} vs {}: {} Avg damage: {}'.format(item[0],item[1], hits/iterations, damageTotal/hits))

def main():
    attackDice = dice.rollDice(3)
    defenseDice = dice.rollDice(5)

    print('{} vs {}'.format(attackDice,defenseDice))

if __name__ == '__main__':
    main()
