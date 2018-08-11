""" Tests to make sure the dice functions keep working. """
from freequest import dice


def test_roll_die():
    assert isinstance(dice.roll_die(), int)


def test_roll_dice():
    assert isinstance(dice.roll_dice(5), list)
