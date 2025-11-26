#coin_flip_random.py  16Jun2025  crs, from coin_flip_loop.py
# test with notepad
# Make it random
# Number flips starting at 1
import random       #bring in support for randomization

# Let's use:
# 0 to represent flipping heads
# 1 to represent flipping tails

nflip = 5       # Number of flips

for n in range(1, nflip+1):     # I like n for 1 based
 flip_result = random.randint(0,1)
 print(n, flip_result)        # position, result
    
