def van_e_pozitiv(lista):
    for e in lista:
        if e > 0:
            return True
    return False

def van_e_pozitiv2(lista):
    return any(e > 0 for e in lista)

def van_e_pozitiv3(lista):
    return any(map(lambda e: e > 0, lista))