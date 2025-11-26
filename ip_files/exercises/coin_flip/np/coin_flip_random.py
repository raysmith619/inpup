#coin_flip_random.py  16Jun2025  crs, from coin_flip_loop.py
# test with notepad
# Make it random
import random       #bring in support for randomization

# Let's use:
# 0 to represent flipping heads
# 1 to represent flipping tails

nflip = 5       # Number of flips

for i in range(nflip):
 flip_result = random.randint(0,1)
 print(i, flip_result)        # position, result
    
