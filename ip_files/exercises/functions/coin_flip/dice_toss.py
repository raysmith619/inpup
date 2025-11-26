# dice_toss.py    30Jun2024  crs, Author
"""
Simple dice toss game
"""
from random import randint

def next_toss():
    """ Return next die value 1..6
    """
    n = randint(1,6)
    return n


if __name__ == "__main__":
    print("dice toss test")
    default_ntoss = 6
    while True:
        inp = input("Enter number of tosses:")
        if inp == "":
            ntoss = default_ntoss
        else:
            ntoss = int(inp)
            default_ntoss = ntoss   # save as new default
        for i in range(ntoss):
            no = i + 1
            die_1 = next_toss()
            die_2 = next_toss()
            print(no,":", die_1, die_2,
                  " total:", die_1+die_2)
    
