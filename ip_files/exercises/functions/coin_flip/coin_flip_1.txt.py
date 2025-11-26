# coin_flip_1.py    30Jun2024  crs, Author
"""
Simple coin flip game
    + Just return "heads"
"""
def next_coin():
    """ Return next coin value "heads", "tails"
    """
    return "heads"

if __name__ == "__main__":
    print("coin_flip test")
    nflip = 3
    for i in range(nflip):
        no = i + 1
        coin_result = next_coin()
        print(no, coin_result)
    
