#heads_tails_short.py
# Short version of heads_tails.py
from random import randint
for i in range(10):
    coin_num = randint(0,1) # 0-heads, 1-tails
    if coin_num == 0: coin = "heads"
    else: coin = "tails"
    print(coin)
    