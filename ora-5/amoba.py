

def kerdez(kerdes: str, ertek_halmaz: list):
	kerdes+=" "
	szoveg_ertekek = []
	for e in ertek_halmaz:
		szoveg_ertekek.append(str(e))
	opciok_szoveg = "Válassz ezek közül: " + ", ".join(szoveg_ertekek)

	while True:
		valasz = input(kerdes)
		if valasz in szoveg_ertekek:
			return valasz
		print(f"Hibás válasz! {opciok_szoveg}")



def jatek():
