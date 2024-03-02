
# Csak listákkal

def metszet(lista1, lista2):
    eredmeny = []
    for elem in lista1:
        if elem in lista2:
            eredmeny.append(elem)
    return eredmeny

# Halmazokkal
def metszet(lista1, lista2):
    return list(set(lista1) & set(lista2))