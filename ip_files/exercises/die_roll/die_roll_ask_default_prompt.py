#die_roll_ask_default_prompt.py    01May2025  crs
# Die rolling program - random roll of one die
# Use simple 
import random

max_roll = 10   # Maximum number of die rolls
prompt = "Enter number of rolls[" + str(max_roll) + "]:"
inp = input(prompt)
if inp != "":
    max_roll = int(inp)
print(__file__)
for i in range(max_roll):
    die_num = random.randint(1,6)
    print(die_num)
    