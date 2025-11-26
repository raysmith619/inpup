#die_roll_game.py    10Apr2025  crs, from die_roll_count.py
# Die rolling game - random roll of one die
# count numbers
import random

bank_roll = 100     # Amount of chips we have
bet = 5             # bet ammount (chips)


print(__file__)
while True:
    inp = input("Enter roll guess:")
    roll_guess = int(inp)
    
    inp = input("Enter bet:")
    bet = int(inp)
    if bet > bank_roll:
        print("Bet too high", bet,">", bank_roll)
        continue
    
    bank_roll -= bet
    
    die_num = random.randint(1,6)
    if die_num == roll_guess:
        print("Congratulations you won!")
        bank_roll += bet*6
        print("New bank roll:", bank_roll)
    else:
        print("Sorry bank roll:", bank_roll)
            