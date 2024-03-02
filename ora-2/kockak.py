from random import randint

while True:
	jatekosSzam = input("Add meg a játékosok számát (2-4): ")
	if jatekosSzam.isdigit():
		jatekosSzam = int(jatekosSzam)
		if 2 <= jatekosSzam <= 4:
			break
		else:
			print("2-4 játékos között kell lennie.")
	else:
		print("Csak számokat adhatsz meg.")

max_pont = 50

jatekos_pontok = [0 for _ in range(jatekosSzam)]


def dob(start=1, end=6):
	return randint(start, end)


def dobal(idx):
	pontszam = 0 
	while True:
		dobna = input("Dobni szeretnél? (i/n)")
		if dobna =="i":
			dobas = dob()
			print(f"A dobásod: {dobas}")
			if dobas == 1:
				print("1-est dobtál. Elvesztetted a pontjaid.")
				pontszam = 0
				break
			else:
				pontszam+=dobas
				print(f"Jelenlegi pontszámod: {pontszam}")
		elif dobna == "n":
			break
		else:
			print("Csak igent vagy nemet adhatsz meg!")
	return pontszam
		


while max(jatekos_pontok) < max_pont:
	for idx in range(jatekosSzam):
		print("\n")
		print(f"{idx+1}. játékos köre")
		print(f"Jelenlegi pontszáma: {jatekos_pontok[idx]}")
		jatekos_pontok[idx] += dobal()
		print(f"{idx+1}. játékos pontszáma: {jatekos_pontok[idx]}")
nyertes_pont = max(jatekos_pontok)
nyertes_idx = jatekos_pontok.index(nyertes_pont)
print(f"A nyertes a {idx+1}. játékos {nyertes_pont} ponttal")




