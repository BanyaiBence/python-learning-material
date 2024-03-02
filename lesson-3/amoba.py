def print_tabla(tabla):
    print("  ", end="")
    print("-" * (4 * len(tabla[0])+1))
    for idx, sor in enumerate(tabla):
        print(f"{idx+1} | ", end="") # sor száma
        print(" | ".join(sor), end=" |\n") # sor elemei, elválasztóval
        print("  ", end="") # elválasztó sor, beljebb húzva
        print("-" * (4 * len(sor)+1)) # elválasztó sor hossza

def nyertes_ellenorzes(tabla, jatekos):
    for i in range(3):
        if all(tabla[i][j] == jatekos for j in range(3)):
            return True
        if all(tabla[j][i] == jatekos for j in range(3)):
            return True
    if all(tabla[i][i] == jatekos for i in range(3)) or all(tabla[i][2 - i] == jatekos for i in range(3)):
        return True
    return False

def kerdez(uzenet, ertek_halmaz):
    while True:
        valasz = input(uzenet)
        if valasz in ertek_halmaz:
            return valasz
        print("Hibás válasz!")


def main():
    tabla = [[" "]*3 for _ in range(3)]
    jatekosok = ['X', 'O']
    aktualis_jatekos = 0

    print("Játsszunk Amőbát!")
    print_tabla(tabla)

    for _ in range(9):  # maximum 9 lépés lehet, mert 3x3-as a tábla
        sor = int(kerdez(f"{jatekosok[aktualis_jatekos]} Írd be a sort (1, 2, 3): ", {"1", "2", "3"})) - 1
        oszlop = int(kerdez(f"{jatekosok[aktualis_jatekos]} Írd be az oszlopot (1, 2, 3): ", {"1", "2", "3"})) - 1

        if tabla[sor][oszlop] == " ":
            tabla[sor][oszlop] = jatekosok[aktualis_jatekos]
            print_tabla(tabla)

            if nyertes_ellenorzes(tabla, jatekosok[aktualis_jatekos]):
                print(f"{jatekosok[aktualis_jatekos]} játékos nyert!")
                break
            aktualis_jatekos = (aktualis_jatekos + 1) % 2
        else:
            print("Ez a pozíció már foglalt. Próbáld újra.")

    else:  
        print("Döntetlen!")

if __name__ == "__main__":
    main()
