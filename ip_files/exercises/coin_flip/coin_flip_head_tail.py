#coin_flip_head_tail.py  16Jun2025  crs,    from coin_flip_random_n.py
# Display "head", "tail"
import random       #bring in support for randomization

# Let's use:
#   0 to represent fliping heads
#   1 to represent fliping tails

nflip = 5       # Number of flips

for n in range(1, nflip+1): # I like i starting from 0, n from 1 
    flip_result = random.randint(0,1)
    if flip_result == 0:
        res = "head"
    if flip_result == 1:
        res = "tail"
    print(n, res)        # "head or tail"
    
