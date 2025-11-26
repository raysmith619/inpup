#coin_flip_head_tail.py  16Jun2025  crs
# test with notepad
# Make it random
# number flips starting with 1
# Show result as "head" or "tail"
import random       #bring in support for randomization

# Let's use:
#  0 to represent flipping heads
#  1 to represent flipping tails

nflip = 5       # Number of flips

for n in range(1, nflip+1):   # start numbering at 1
 flip_result = random.randint(0,1)
 if flip_result == 0:
  res = "head"
 if flip_result == 1:
  res = "tail"
 print(n, res)        # position, result
    
