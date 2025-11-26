#dice_roll.py    31Jan2025  crs
# Die rolling program - random roll of one die
import random
print(__file__)
max_roll = 10        # number of rolls
for i in range(max_roll):
    die1_num = random.randint(1,6)
    die2_num = random.randint(1,6)
    sum_dice = die1_num + die2_num
    print(f"{die1_num} {die2_num} {sum_dice}")
    