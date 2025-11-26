#heads_tails.py
# Simple demonstration of coin flipping program
from random import randint
max_flip = 10
nflip = 0
while nflip < max_flip:
    nflip = nflip + 1
    coin_num = randint(0,1) # 0-heads, 1-tails
    if coin_num == 0:
        coin = "heads"
    else:
        coin = "tails"
    print(coin)
    