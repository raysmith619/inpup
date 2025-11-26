#heads_tails_shorter.py
# Short version of heads_tails.py
from random import randint
for i in range(10):
    coin = "heads" if randint(0,1) == 0 else "tails" # 0-heads, 1-tails
    print(coin)
    