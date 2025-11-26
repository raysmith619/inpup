#die_roll_count_large.py    26Jan2025  crs
# Die rolling program - random roll of one die
# count numbers
import random

max_roll = 10   # Maximum number of die rolls
inp = input("Enter number of rolls:")
max_roll = int(inp)
die_num_counts = {}     # Dictionary by rolled number of counts
print(__file__)
for i in range(max_roll):
    die_num = random.randint(1,6)
    if die_num not in die_num_counts:
        die_num_counts[die_num] = 0
    die_num_counts[die_num] += 1        # add one
    print(i+1, die_num, die_num_counts[die_num])
    