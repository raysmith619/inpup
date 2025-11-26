#die_roll_nums.py    31Jan2025  crs
# Die rolling program - random roll of one die
import random
print(__file__)
max_roll = 5000       # number of rolls
die_roll_nums = {}  # Number of roles for each die side
for i in range(max_roll):
    die_num = random.randint(1,5+1)
    if die_num not in die_roll_nums:
        die_roll_nums[die_num] = 0  # Initialize before first use
    die_roll_nums[die_num] += 1     # count each time
    if i > max_roll-6:
        print(i+1, die_num, die_roll_nums[die_num])

print(f"Die roll counts for {max_roll} rolls")
for n in range(1, 6+1):
    if n in die_roll_nums:
        print(n, die_roll_nums[n])