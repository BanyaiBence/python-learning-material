# 2. Készíts egy függvényt, amely visszaad egy véletlenszerű számot 1 és 6 között, de a függvénynek legyen egy alapértelmezett paramétere, amely megadja, hogy hány oldalú kockával dobunk.

def dob(oldalak=6):
    import random
    return random.randint(1, oldalak)