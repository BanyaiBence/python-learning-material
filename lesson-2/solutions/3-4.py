# 3. Kérj be a felhasználótól egy számot és ellenőrizd le, hogy csak számokat adott-e meg.

def szamot_ker():
    szam = input("Kérlek, adj meg egy számot: ")
    while not szam.isdigit():
        print("Ez nem egy szám!")
        szam = input("Kérlek, adj meg egy számot: ")
    return int(szam)