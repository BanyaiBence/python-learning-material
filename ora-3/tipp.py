from random import randint


def beker_szam(uzenet):
	while True:
		try:
			szam = int(input(uzenet))
			return szam
		except ValueError:
			print("Ez nem egy szám!")

def rekord_olvasas():
	try:
		with open("rekord.txt", "r") as f:
			return int(f.read())
	except FileNotFoundError:
		return None

def rekord_iras(pontszam):
	with open("rekord.txt", "w") as f:
		f.write(str(pontszam))

def jatek():
	rekord = rekord_olvasas()
	if rekord is None:
		print("Köszöntelek a játékban!")
	else:
		print(f"Üdv újra a játékban! Az eddigi rekord: {rekord}")

	titkos_szam = randint(1, 100)
	probalkozasok = 0
	while True:
		tipp = beker_szam("Tippeld meg a titkos számot ( 1 és 100 között): ")
		if tipp < 1 or tipp > 100:
			print("1 és 100 között legyen a válaszod!")
			continue
		probalkozasok+=1

		if tipp < titkos_szam:
			print("Túl alacsony!")
		elif tipp > titkos_szam:
			print("Túl magas!")
		else:
			print(f"Gratulálok! {probalkozasok} próbálkozásra sikerült kitalálnod a számot!")
			if rekord is None or probalkozasok < rekord:
				print("Új rekord")
				rekord_iras(probalkozasok)
			break

