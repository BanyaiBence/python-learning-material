
# Csak listákkal
def unio(lista1, lista2):
    eredmeny = []
    for elem in lista1:
        if elem not in eredmeny:
            eredmeny.append(elem)
    for elem in lista2:
        if elem not in eredmeny:
            eredmeny.append(elem)
    return eredmeny

# Halamzokkal
def unio(lista1, lista2):
    return list(set(lista1) | set(lista2))
