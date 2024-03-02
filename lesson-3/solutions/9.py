def listat_olvas(fajl_nev):
    with open(fajl_nev, "r") as f:
        return f.read().splitlines()
    
def listat_iras(fajl_nev, lista):
    with open(fajl_nev, "w") as f:
        for elem in lista:
            f.write(elem + "\n")