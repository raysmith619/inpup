#dice.py
""" Simple dice play
    + Start with simple random die
"""
from random import randint
die_size = 6
for i in range(die_size):
    roll = i+1
    roll_val = randint(1, die_size)
    print("roll:", roll, roll_val)
