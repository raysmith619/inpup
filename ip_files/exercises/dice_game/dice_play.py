#dice_play.py
""" Simple dice play
Rules:
    An even money bet, made
    on the first roll of the
    dice (known as the “come out roll”).
    You win if a 7 or 11 roll,
    or lose if 2, 3, or 12
    roll (known as “craps”).
    Any other number that rolls
    becomes the “point” and the
    point must roll again
    before a 7 to win.
"""
from random import randint

def_ndie = 2
def_die_size = 6
def dice_roll(ndie=def_ndie, die_size=def_die_size):
    """ Return values of dice
    :ndie: number of die default: 2
    :die_size: number of faces to each die
            default: 6
    :returns: list of rolled values
    """
    die_vals = []
    for i in range(ndie):
        die_vals.append(randint(1,die_size))
    return die_vals

def dice_game():
    """ Play one game
    :returns: True if win, else False
    """
    roll1 = dice_roll()
    roll1_sum = sum(roll1)
    print("\nFirst roll:", roll1, "giving", roll1_sum)
    if roll1_sum == 7 or roll1_sum == 11:
        print(roll1, "-", roll1_sum, "wins on first roll")
        return True

    if roll1_sum in [2,3,12]:
        print(roll1, "-", roll1_sum, "looses - craps")
        return False

    nroll = 1
    point = roll1_sum
    print("First roll:", roll1, "- The point is", point)
    while True:
        nroll += 1  # Count rolls, including first
        roll = dice_roll()
        roll_sum = sum(roll)
        if roll_sum == point:
            print(roll, "Point made on roll", nroll)
            return True
        
        print("roll:", nroll, "got", roll,
              "looking for", point)

while dice_game():
    pass
