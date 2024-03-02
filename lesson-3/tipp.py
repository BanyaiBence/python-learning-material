import random

def beker_szam(uzenet):
    while True:
        try:
            szam = int(input("Adj meg egy számot: "))
            return szam
        except ValueError:
            print("Ez nem egy szám!")

def rekord_olvasas():
    try:
        with open("rekord.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return None

def rekord_iras(pontszam):
    with open("rekord.txt", "w") as file:
        file.write(str(pontszam))

def jatek():
    rekord = rekord_olvasas()
    if rekord is None:
        print("Köszöntelek a játékban!")
    else:
        print(f"Üdv újra a játékban! Az eddigi rekord: {rekord}")

    titkos_szam = random.randint(1, 100)
    probalkozasok = 0

    while True:
        tipp = beker_szam("Tippeld meg a számot (1 és 100 között): ")
        probalkozasok += 1

        if tipp < titkos_szam:
            print("Túl alacsony!")
        elif tipp > titkos_szam:
            print("Túl magas!")
        else:
            print(f"Gratulálok! {probalkozasok} próbálkozásra sikerült kitalálnod a számot!")
            if rekord is None or probalkozasok < rekord:
                print("Új rekord!")
                rekord_iras(probalkozasok)
            break

if __name__ == "__main__":
    jatek()
