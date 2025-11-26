#die_roll_random.py    31Jan2025  crs
# Die rolling program - random roll of one die
import random
print(__file__)
max_roll = 5        # number of rolls
for i in range(max_roll):
    die_num = random.randint(1,6)
    print(die_num)
    