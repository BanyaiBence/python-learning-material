# 7. Készíts egy függvényt, amely visszaad egy listát 1-től 10-ig, de ha a szám osztható 3-mal, akkor a szám helyett adjon vissza egy 0-t.

def nullazo_lista():
    return [0 if i % 3 == 0 else i for i in range(1, 11)]