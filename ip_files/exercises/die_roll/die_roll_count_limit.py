#die_roll_count_limit.py    26Jan2025  crs
# Die rolling program - random roll of one die
# count numbers
# Limit printing to a small number
import random

max_roll = 10   # Maximum number of die rolls
limit_print = 10    # limit printing to last number
inp = input("Enter number of rolls:")
max_roll = int(inp)

die_num_counts = {}     # Dictionary by rolled number of counts
print(__file__)
for i in range(max_roll):
    die_num = random.randint(1,6)
    if die_num not in die_num_counts:
        die_num_counts[die_num] = 0
    die_num_counts[die_num] += 1        # add one
    if i > max_roll - limit_print:
        print(i+1, die_num, die_num_counts[die_num])
    