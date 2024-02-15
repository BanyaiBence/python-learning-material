# 10. Készíts egy függvényt ami beszúr egy element pont a lista közepére.

def beszur(lista, elem):
    lista.insert(len(lista) // 2, elem)
    return lista