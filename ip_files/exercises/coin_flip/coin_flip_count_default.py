#coin_flip_count_default.py  16Jun2025  crs, from coin_flip_count_ask.py
# ask number with default
import random       #bring in support for randomization

# Let's use:
#   0 to represent fliping heads
#   1 to represent fliping tails

nflip = 5       # Number of flips
nhead = 0       # Track number of heads
ntail = 0       # Count of tails
prompt = f"How many flips[{nflip}]:"
inp = input(prompt)
if inp == "":
    inp = str(nflip)
nflip = int(inp)
for n in range(1, nflip+1): # I like i starting from 0, n from 1 
    flip_result = random.randint(0,1)
    res = "head" if flip_result == 0 else "tail"
    if flip_result == 0:    # Use internal value
        nhead += 1
    elif flip_result == 1:
        ntail += 1
        
    print(n, res, " heads:", nhead, "  tails:", ntail)        # "head or tail"
    
