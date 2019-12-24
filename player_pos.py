import random

def spawnpos(dimension):
    if(dimension == "x"): return random.randint(2, 48) * 16
    if(dimension == "y"): return random.randint(2, 28) * 16