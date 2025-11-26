#die_roll_ask_default_try.py    01May2025  crs
# Die rolling program - random roll of one die
# Use try/except for typos 
import random

max_roll = 10   # Maximum number of die rolls
prompt = "Enter number of rolls[" + str(max_roll) + "]:"
while True:
    inp = input(prompt)
    if inp != "":
            try:
                max_roll = int(inp)
                break   # OK
            except:
                print("I don't understand", inp,"please try again")
        
print(__file__)
for i in range(max_roll):
    die_num = random.randint(1,6)
    print(die_num)
    