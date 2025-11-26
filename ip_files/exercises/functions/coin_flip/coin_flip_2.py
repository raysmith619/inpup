# coin_flip_2.py    30Jun2024  crs, Author
"""
Simple coin flip game
    + Just return "heads"
    + Randomize return
"""
from random import randint

def next_coin():
    """ Return next coin value "heads", "tails"
    """
    n = randint(0,1)
    if n == 0:
        return "heads"
    if n  == 1:
        return "tails"

if __name__ == "__main__":
    print("coin_flip test")
    inp = input("Enter number of flips:")
    nflip = int(inp)
    for i in range(nflip):
        no = i + 1
        coin_result = next_coin()
        print(no, coin_result)
    
