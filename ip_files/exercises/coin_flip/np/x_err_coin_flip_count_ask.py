#x_err_coin_flip_count_ask.py  16Jun2025  crs
# test with notepad
# Make it random
# number flips starting with 1
# count head, tail
# ask number of flips
x import random       #bring in support for randomization

# Let's use:
#  0 to represent flipping heads
#  1 to represent flipping tails
nhead = 0
ntail = 0

nflip = 5       # Number of flips
inp = input("Enter number of flips:")
nflip = int(inp)
for n in range(1, nflip+1):   # start numbering at 1
 flip_result = random.randint(0,1)
 if flip_result == 0:
  res = "head"
  nhead += 1          # increment number of heads
 if flip_result == 1:
  res = "tail"
  ntail += 1
 print("flip", n, "is", res, "the counts are", "heads", nhead, " tails", ntail)        # position, result
 
