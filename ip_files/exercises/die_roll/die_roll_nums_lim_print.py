#die_roll_nums.py    31Jan2025  crs
# Die rolling program - random roll of one die
import random
print(__file__)
max_roll = 50000000        # number of rolls
die_roll_nums = {}  # Number of roles for each die side
for i in range(max_roll):
    die_num = random.randint(1,6)
    if die_num not in die_roll_nums:
        die_roll_nums[die_num] = 0  # Initialize before first use
    die_roll_nums[die_num] += 1     # count each time
    if i > max_roll-10:         # Only print last few
        print(die_num)

print(f"Die roll counts for {max_roll} rolls")
for i in range(6):
    n = i + 1       # range 0-max to die 1-6
    if n in die_roll_nums:
        die_roll_count = die_roll_nums[n]
        print(f"{n} {die_roll_count}")