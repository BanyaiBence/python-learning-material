

def indul():
	while True:
		be = input("1(+), 2(-), 3(/), 4(*), 5(kilep)")
		if not be.isdigit():
			print("Nem számot adtál meg!")
			continue
		be = int(be)
		if not (1 <= be <= 5):
			print("1 és 5 között számot adj meg!")
			continue
		return be

def ker_szamot(uzenet):
	while True:
		szam = input(uzenet)
		if not szam.isdigit():
			print("Számot adhatsz csak meg!")
			continue
		return int(szam)


def muvelet(n):
	if n == 5:
		quit()
	szam1 = ker_szamot("Add meg az első számot! ")
	szam2 = ker_szamot("Add meg a második számot! ")
	if n == 1:
		return szam1+szam2
	if n == 2:
		return szam1-szam2
	if n == 3:
		return round(szam1/szam2, 2)
	if n == 4:
		return szam1*szam2
	

while True:
	m = indul()
	eredmeny = muvelet(m)
	print(f"eredmeny: {eredmeny}\n")





