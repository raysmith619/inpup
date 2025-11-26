#coin_flip_count_ask.py  16Jun2025  crs
# ask number of rolls
import random       #bring in support for randomization

# Let's use:
#   0 to represent fliping heads
#   1 to represent fliping tails

nflip = 5       # Number of flips
nhead = 0       # Track number of heads
ntail = 0       # Count of tails
inp = input("How many flips:")
nflip = int(inp)
for n in range(1, nflip+1): # I like i starting from 0, n from 1 
    flip_result = random.randint(0,1)
    if flip_result == 0:    # Use internal value
        res = "head"
        nhead += 1
    elif flip_result == 1:
        res = "tail"
        ntail += 1
        
    print(n, res, " heads:", nhead, "  tails:", ntail)        # "head or tail"
    
