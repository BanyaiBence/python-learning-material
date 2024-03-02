def elso_nem_ismetlodo(lista):
    # A feladatot úgy oldjuk meg, hogy egy dictionary-be eltároljuk, hogy egy elem hányszor szerepel a listában
    ismetlodesek = {}
    for elem in lista:
        if elem in ismetlodesek:
            ismetlodesek[elem] += 1
        else:
            ismetlodesek[elem] = 1
    
    for elem in lista:
        if ismetlodesek[elem] == 1:
            return elem
    return None # Ez elhagyható, mert ha nincs return, akkor is None-t ad vissza a függvény, de így szebb
