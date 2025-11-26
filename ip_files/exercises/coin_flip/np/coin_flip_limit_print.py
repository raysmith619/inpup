#coin_flip_limit_print.py  16Jun2025  crs
# test with notepad
# Make it random
# number flips starting with 1
# count head, tail
# ask number of flips, with default
# loop running
# limit printing to last few filps

import random       #bring in support for randomization

# Let's use:
#  0 to represent flipping heads
#  1 to represent flipping tails

nflip = 5       # Number of flips, kept recent

while True:
 nhead = 0
 ntail = 0

 prompt = f"Enter number of flips[{nflip}]:"
 inp = input(prompt)
 if inp == "":
  inp = str(nflip)    # string of nflip
 nflip = int(inp)
 for n in range(1, nflip+1):   # start numbering at 1
  flip_result = random.randint(0,1)
  if flip_result == 0:
   res = "head"
   nhead += 1          # increment number of heads
  if flip_result == 1:
   res = "tail"
   ntail += 1
  if n > nflip - 5:   # Print just last few flips
   print("flip", n, "is", res, "the counts are", nhead,
         "heads", ntail, " tails")        # position, result
 
