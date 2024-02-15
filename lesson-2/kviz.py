import random

def indul():
    print("Köszöntelek a kvízemben!")
    jatszik = input("Szeretnél játszani? (igen/nem)")
    
    while jatszik.lower() not in ["igen", "nem"]:
        print("Kérlek, csak 'igen' vagy 'nem' választ adj meg!")
        jatszik = input("Szeretnél játszani? (igen/nem)")


    if jatszik.lower() == "nem":
        print("Köszönöm, hogy eljöttél!")
        return False
    
    elif jatszik.lower() == "igen":
        print("Remek! Akkor kezdjük el a játékot!")
        return True

def kerdez(kerdes, valasz):
    global kerdesSzam
    kerdesSzam += 1
    bemenet = input(f"{kerdesSzam}. {kerdes}")
    if bemenet.lower() == valasz:
        print('Helyes!')
        return 1
    else:
        print("Helytelen!" + f" A helyes válasz: '{valasz}'.")
        return 0
    

kerdesek = [("Mit rövidít a CPU? ", "central processing unit"),
            ("Mit rövidít a GPU? ", "graphics processing unit"),
            ("Mit rövidít a RAM? ", "random access memory"),
            ("Mit rövidít a PSU? ", "power supply"),
            ("Mit rövidít a HDD? ", "hard disk drive"),
            ("Mit rövidít az SSD? ", "solid state drive"),
            ("Mit rövidít a LAN? ", "local area network"),
            ("Mit rövidít a WAN? ", "wide area network"),
            ("Mit rövidít a WLAN? ", "wireless local area network"),
            ("Mit rövidít a BIOS? ", "basic input/output system"),
            ("Mit rövidít az OS? ", "operating system"),
            ("Mit rövidít a GUI? ", "graphical user interface"),
            ("Mit rövidít a CLI? ", "command line interface"),
            ("Mit rövidít a API? ", "application programming interface"),
            ("Mit rövidít a HTTP? ", "hypertext transfer protocol"),
            ("Mit rövidít az URL? ", "uniform resource locator"),
            ("Mit rövidít a HTML? ", "hypertext markup language"),
            ("Mit rövidít a CSS? ", "cascading style sheets"),
            ("Mit rövidít a JS? ", "javascript"),
            ("Mit rövidít a SQL? ", "structured query language")
            ]


if not indul():
    quit()

kerdesSzam = 0

pontok = 0

while kerdesek:
    kerdes = random.choice(kerdesek)
    kerdesek.remove(kerdes)
    pontok += kerdez(kerdes[0], kerdes[1])

print(str(pontok) + " kérdést találtál el!")
print(str(round((pontok / kerdesSzam) * 100, 1)) + "%-os eredményt értél el!")