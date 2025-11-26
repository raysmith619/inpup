#die_roll_ask_max_roll.py    26Jan2025  crs
# Die rolling program - random roll of one die
import random

max_roll = 10   # Maximum number of die rolls
inp = input("Enter number of rolls:")
max_roll = int(inp)
print(__file__)
for i in range(max_roll):
    die_num = random.randint(1,6)
    print(die_num)
    