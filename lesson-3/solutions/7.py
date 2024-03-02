def negyzetek(lista):
    return [x ** 2 for x in lista]

def negyzetek2(lista):
    return list(map(lambda x: x ** 2, lista))

def negyzetek3(lista):
    eredmeny = []
    for x in lista:
        eredmeny.append(x ** 2)
    return eredmeny
