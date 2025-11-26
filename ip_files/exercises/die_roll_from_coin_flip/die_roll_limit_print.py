#die_roll_limit_print.py  07Jul2025  crs, from coin_flip_limit_print.py
# limit printing to last few
# Develop from coin_flip
import random       #bring in support for randomization

# Generalize with variable
ndie_face =  6  # die values 1-ndie_face


nroll = 5       # Number of rolls

while True:
    nroll_counts = {}       # Dictionary of die roll counts
    for n in range(1, ndie_face+1):
        nroll_counts[n] = 0 # Zero out count
    prompt = f"How many rolls[{nroll}]:"
    inp = input(prompt)
    if inp == "":
        inp = str(nroll)
    nroll = int(inp)
    for n in range(1, nroll+1):
        roll_result = random.randint(1, ndie_face)
        nroll_counts[roll_result] += 1
        if n > nroll - 5:    
            print(f"roll {n} is {roll_result} giving ", end="  ")   # no newline
            for nf in range(1, ndie_face+1):        # All on same line
                print(f"{nroll_counts[nf]} {nf}s,", end= " ")       # no newline
            print()
    
