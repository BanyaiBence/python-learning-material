def mind_pozitiv_e(lista):
    for e in lista:
        if e < 0:
            return False
    return True

def mind_pozitiv_e2(lista):
    return all(e >= 0 for e in lista)

def mind_pozitiv_e3(lista):
    return all(map(lambda e: e >= 0, lista))
