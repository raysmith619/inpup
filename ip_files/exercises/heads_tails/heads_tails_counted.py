#heads_tails_counted.py
# Simple demonstration of coin flipping program
# Count number of heads,tails
from random import randint
max_flip = 10000
nflip = 0
n_head = 0  # Number of heads
n_tail = 0
prev_num = -1   # previous flip
n_run = 0       # run of repeats
high_run = 0    # highest run
while nflip < max_flip:
    nflip = nflip + 1
    coin_num = randint(0,1) # 0-heads, 1-tails
    if coin_num == 0:
        n_head = n_head + 1
        coin = "heads"
    else:
        n_tail = n_tail + 1
        coin = "tails"
    print(nflip, coin, " H:", n_head, " T:", n_tail)
    prev_num = coin_num