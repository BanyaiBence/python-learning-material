def csak_parosak(lista):
    return [x for x in lista if x % 2 == 0]

def csak_parosak2(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

def csak_parosak3(lista):
    eredmeny = []
    for x in lista:
        if x % 2 == 0:
            eredmeny.append(x)
    return eredmeny