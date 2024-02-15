<link href="../assets/styles/style_1.css" rel="stylesheet"/>
<img src="../assets/lessons/lesson-2/dices_1.png" width=200px>

# A mai fő témánk, gyakorlás és a listák

# Tartalomjegyzék
1. [Alapértelmezett paraméterek](#id-1)
2. [isdigit() metódus](#id-2)
3. [Listák generálása](#id-3)
4. [range() függvény](#id-4)
5. [lower() és upper() metódus](#id-5)
6. [random.choice() metódus](#id-6)
7. [remove() metódus](#id-7)
8. [count() metódus](#id-8)
9. [sort() metódus](#id-9)
10. [reverse() metódus](#id-10)
11. [append() metódus](#id-11)
12. [extend() metódus](#id-12)
13. [insert() metódus](#id-13)
14. [pop() metódus](#id-14)
15. [clear() metódus](#id-15)
16. [copy() metódus](#id-16)
17. [index() metódus](#id-17)
18. [list() függvény](#id-18)
19. [len() függvény](#id-19)
20. [max() függvény](#id-20)
21. [min() függvény](#id-21)
22. [sum() függvény](#id-22)
23. [Mi az, hogy iterálható?](#id-23)
24. [Tupple](#id-24)
25. [Set](#id-25)
26. [Dictionary](#id-26)
27. [Lista indexelős trükkök](#id-27)
28. [Feladatok](#id-28)
29. [Megoldások](#id-29)
30. [Összefoglaló](#id-31)

# A játékról:
- A játékot 2 vagy 4 játékos játszhatja.
- A játék folyamán a játékosok körönként dobhatnak egy kockával.
- A dobás eredménye hozzáadódik a játékos pontjaihoz.
- Ha a játékos 1-et dob, akkor az összes eddigi pontja elveszik és a következő játékos következik.
- Ha a játékos úgy dönt, hogy megáll, akkor a pontjai hozzáadódnak a játékos összpontszámához és a következő játékos következik.

# Segítség a kódhoz:
- ## A `random` modul segítségével tudunk véletlen számokat generálni.
    ```python
    import random

    roll = random.randint(1, 6)
    ```
    - `random.randint(a, b)` -> Visszaad egy véletlenszerű egész számot az `a` és `b` között. 
    - `random.choice(lista)` -> Visszaad egy véletlenszerű elemet a listából.

- ## <div id="id-1"/>A függvényeknek lehetnek alapértelmezett paraméterei 
    ```python
    import random

    def dob(oldal_szam=6):
        roll = random.randint(1, oldal_szam)

        return roll
    ```
    - A függvényeknek lehetnek olyan paraméterei, amelyeknek alapértelmezett értéket adunk. Ha a függvényt meghívjuk és nem adunk meg új értéket az alapértelmezett paraméternek, akkor az alapértelmezett értékkel fogja végrehajtani a függvényt. 
    - Példa: `def dob(oldalSzam=6):`  
    - Ha nem adunk meg értéket a `dob` függvénynek, akkor az `oldalSzam` értéke 6 lesz.
    - Ha megadunk értéket a `dob` függvénynek, akkor az `oldalSzam` értéke az általunk megadott érték lesz. 

- ## <div id="id-2"/> Az `isdigit()` metódus segítségével ellenőrizhetjük, hogy egy string csak számokat tartalmaz-e. 
    ```python
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
    ```
    - Példa: `szam = "123"`  `szam.isdigit()`  -> True 
    - Példa: `szam = "123a"`  `szam.isdigit()`  -> False 
    - Így többet nem kell listát használnunk ehhez az ellenőrzéshez.

- ## <div id="id-3"/>Tudunk listákat generálni
    ```python
    jatekos_pontok = [0 for _ in range(jatekosSzam)]
    ```
    - Példa: `szamok = [i for i in range(1, 11)]`  -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    - #### Egy listában tudunk feltételes kifejezéseket is használni.
        - Példa: `szamok = [i for i in range(1, 11) if i % 2 == 0]`  -> [2, 4, 6, 8, 10]
            - A feltétel csak akkor teljesül, ha az `i` értéke páros.
        - Példa: `szamok = [i if i % 2 == 0 else 0 for i in range(1, 11)]`  -> [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
            - Ha az `i` értéke páros, akkor az `i` értékét adja a listához, ha nem, akkor 0-t ad a listához.
    - > Érdekesség: A generált listák elemei csak akkor dolgozódnak fel, amikor hozzáférünk az adott elemhez. Ez azt jelenti, hogy a generált listák nem foglalnak sok memóriát, mivel csak a szabályt tárolják, amely alapján a lista elemei generálódnak.
- ## <div id="id-4"/> A `range()` függvény
    - A `range(a, b)` függvény visszaad egy sorozatot az `a` és `b` közötti számokkal.
    - Példa: `szamok = list(range(1, 11))`  -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    - > Megjegyzés: A `range()` függvény nem ad vissza listát, hanem egy `range` objektumot. Ha listává akarjuk alakítani, akkor a `list()` függvényt kell használnunk.
- ## <div id="id-5"/>`lower()` metódus
    - A `string.lower()` metódus visszaadja a string kisbetűs változatát.
    - Példa: `szoveg = "Hello"`  `szoveg.lower()`  -> "hello"
    - > Megjegygzés: A `string.upper()` metódus visszaadja a string nagybetűs változatát.
- ## <div id="id-6"/>`random.choice()` metódus
    - A `random.choice(lista)` metódus visszaad egy véletlenszerű elemet a listából.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `random.choice(szamok)`  -> 3
    - > Megjegyzés: A `random.choice()` metódus csak akkor működik, ha a `random` modult importáltuk.
- ## <div id="id-7"/>`remove()` metódus
    - A `list.remove(elem)` metódus eltávolítja az `elem`-et a listából.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.remove(3)`  -> [1, 2, 4, 5]
    - Ha az `elem` nem szerepel a listában, akkor hibát fog dobni.
    - > Megjegyzés: Ha az `elem` többször szerepel a listában, akkor csak az első előfordulását fogja eltávolítani.
- ## <div id="id-8"/>`count()` metódus
    - A `list.count(elem)` metódus visszaadja, hogy az `elem` hányszor szerepel a listában.
    - Példa: `szamok = [1, 2, 3, 3, 4, 5]`  `szamok.count(3)`  -> 2
    - Ha az `elem` nem szerepel a listában, akkor 0-t fog visszaadni.
- ## <div id="id-9"/>`sort()` metódus
    - A `list.sort()` metódus rendezni fogja a listát.
    - Példa: `szamok = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`  `szamok.sort()`  -> [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    - > Megjegyzés: A `list.sort()` metódus nem ad vissza semmit, csak a listát fogja rendezni.
- ## <div id="id-10"/>`reverse()` metódus
    - A `list.reverse()` metódus megfordítja a listát.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.reverse()`  -> [5, 4, 3, 2, 1]
    - > Megjegyzés: A `list.reverse()` metódus nem ad vissza semmit, csak a listát fogja megfordítani.
- ## <div id="id-11"/>`append()` metódus
    - A `list.append(elem)` metódus hozzáadja az `elem`-et a listához.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.append(6)`  -> [1, 2, 3, 4, 5, 6]
    - > Megjegyzés: A `list.append()` metódus csak egy elemet tud hozzáadni a listához.
- ## <div id="id-12"/>`extend()` metódus
    - A `list.extend(lista)` metódus hozzáadja a `lista` elemeit a listához.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.extend([6, 7, 8])`  -> [1, 2, 3, 4, 5, 6, 7, 8]
    - > Megjegyzés: A `list.extend()` metódus csak egy listát tud hozzáadni a listához.
- ## <div id="id-13"/>`insert()` metódus
    - A `list.insert(index, elem)` metódus beszúrja az `elem`-et a listába az `index` indexű helyre.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.insert(2, 6)`  -> [1, 2, 6, 3, 4, 5]
    - > Megjegyzés: Ha az `index` nagyobb, mint a lista hossza, akkor az `elem` a lista végére kerül.
- ## <div id="id-14"/>`pop()` metódus
    - A `list.pop(index)` metódus eltávolítja az `index` indexű elemet a listából és visszaadja azt.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.pop(2)`  -> 3
    - Ha nem adunk meg indexet, akkor az utolsó elemet fogja eltávolítani.
    - > Megjegyzés: Ha az `index` nagyobb, mint a lista hossza, akkor hibát fog dobni.
- ## <div id="id-15"/>`clear()` metódus
    - A `list.clear()` metódus törli a lista elemeit.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `szamok.clear()`  -> []
    - > Megjegyzés: A `list.clear()` metódus nem ad vissza semmit, csak a listát fogja törölni.
- ## <div id="id-16"/>`copy()` metódus
    - A `list.copy()` metódus visszaad egy másolatot a listáról.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masolat = szamok.copy()`  -> [1, 2, 3, 4, 5]
    - > Megjegyzés: Később fogunk beszélni a másolatokról részletesebben.
- ## <div id="id-17"/>`index()` metódus
    - A `list.index(elem)` metódus visszaadja az `elem` indexét a listában.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `index = szamok.index(3)`  -> 2
    - Ha az `elem` nem szerepel a listában, akkor hibát fog dobni.
    - > Emlékeztető: A listák indexelése 0-tól kezdődik.
- ## <div id="id-18"/>`list()` függvény
    - A `list()` függvény visszaad egy listát.
    - Példa: `szamok = list((1, 2, 3, 4, 5))`  -> [1, 2, 3, 4, 5]
    - > Megjegyzés: A `list()` függvény csak olyan objektumokat tud listává alakítani, amelyek iterálhatóak.
- ## <div id="id-19"/>`len()` függvény
    - A `len()` függvény visszaadja a lista hosszát.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `hossz = len(szamok)`  -> 5
    - > Megjegyzés: A `len()` függvény csak olyan objektumok hosszát tudja visszaadni, amelyek iterálhatóak.
- ## <div id="id-20"/>`max()` függvény
    - A `max()` függvény visszaadja a lista legnagyobb elemét.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `max = max(szamok)`  -> 5
    - > Megjegyzés: A `max()` függvény csak olyan objektumok legnagyobb elemét tudja visszaadni, amelyek iterálhatóak.
- ## <div id="id-21"/>`min()` függvény
    - A `min()` függvény visszaadja a lista legkisebb elemét.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `min = min(szamok)`  -> 1
    - > Megjegyzés: A `min()` függvény csak olyan objektumok legkisebb elemét tudja visszaadni, amelyek iterálhatóak.
- ## <div id="id-22"/>`sum()` függvény
    - A `sum()` függvény visszaadja a lista elemeinek összegét.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `osszeg = sum(szamok)`  -> 15
    - > Megjegyzés: A `sum()` függvény csak olyan objektumok összegét tudja visszaadni, amelyek iterálhatóak.
- ## <div id="id-23"/> Mi az, hogy iterálható?
    - Az iterálható objektumok olyan objektumok, amelyeknek van eleme és ezeket az elemeket sorban le tudjuk kérdezni.
    - Példa: listák, stringek, tuple-ök, szótárak, halmazok
    - > Megjegyzés: Az iterálható objektumokról később fogunk még részletesebben beszélni.
- ## <div id="id-24"/>Tupple
    - A tuple egy olyan adatszerkezet, amelyben tárolhatunk több elemet.
    - A tuple elemeit zárójelek közé írjuk és vesszővel választjuk el őket.
    - Példa: `szamok = (1, 2, 3, 4, 5)`
    - A tuple elemei nem módosíthatóak, tehát nem tudjuk megváltoztatni a tuple elemeit.
- ## <div id="id-25"/>Set
    - A set egy olyan adatszerkezet, amelyben tárolhatunk több elemet.
    - A set elemeit kapcsos zárójelek közé írjuk és vesszővel választjuk el őket.
    - Példa: `szamok = {1, 2, 3, 4, 5}`
    - A set elemei nem rendezettek és nem lehet benne többször ugyanaz az elem.
    - A set halmazt jelent.
- ## <div id="id-26"/>Dictionary
    - A dictionary egy olyan adatszerkezet, amelyben kulcs-érték párokat tárolhatunk.
    - A dictionary elemeit kapcsos zárójelek közé írjuk és vesszővel választjuk el őket.
    - Példa: `szamok = {"egy": 1, "ketto": 2, "harom": 3}`
    - A dictionary jelentése szótár.
    - A dictionary kulcsai nem lehetnek azonosak.
    -> Megjegyzés: A dictionary-ról később fogunk még részletesebben beszélni.

- ## <div id="id-27"/>Lista indexelős trükkök
    - A lista elemeit lehet indexelni, tehát hozzáférni az elemekhez.
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `elsoElem = szamok[0]`  -> 1
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `utolsoElem = szamok[-1]`  -> 5
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masodikElem = szamok[1]`  -> 2
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masodiktolNegyedikElem = szamok[1:4]`  -> [2, 3, 4]
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `elsoNegyElem = szamok[:4]`  -> [1, 2, 3, 4]
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masodiktolUtolsoElem = szamok[1:]`  -> [2, 3, 4, 5]
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masodiktolUtolsoElottiElem = szamok[1:-1]`  -> [2, 3, 4]
    - Példa: `szamok = [1, 2, 3, 4, 5]`  `masodiktolUtolsoElemKettesevel = szamok[1:-1:2]`  -> [2, 4]
    - A [::-1] kifejezés megfordítja a listát. Mert ez a lista végétől kezdi indexelni és -1-esével lépked.
    - > Megjegyzés: A lista indexelése 0-tól kezdődik és a negatív indexekkel a lista végétől tudunk indexelni. A `:` jel után megadhatjuk, hogy meddig szeretnénk indexelni és hogy hányasával szeretnénk lépkedni.

# <div id="id-28"/> Feladatok
1. Készíts egy függvényt, amely visszaad egy véletlenszerű számot 1 és 6 között.
2. Készíts egy függvényt, amely visszaad egy véletlenszerű számot 1 és 6 között, de a függvénynek legyen egy alapértelmezett paramétere, amely megadja, hogy hány oldalú kockával dobunk.
3. Kérj be a felhasználótól egy számot és ellenőrizd le, hogy csak számokat adott-e meg.
4. Kérj be a felhasználótól egy számot és ellenőrizd le, hogy csak számokat adott-e meg. Ha igen, akkor add vissza a számot, ha nem, akkor kérj be újra egy számot.
5. Készíts egy függvényt, amely visszaad egy listát 1-től 10-ig.
6. Készíts egy függvényt, amely visszaad egy listát 1-től 10-ig, de csak a páros számokat.
7. Készíts egy függvényt, amely visszaad egy listát 1-től 10-ig, de ha a szám osztható 3-mal, akkor a szám helyett adjon vissza egy 0-t.
8. Készíts egy olyan függvényt, amely kiszámolja egy lista legnagyobb és legkisebb elemének a különbségét.
9. Készíts egy olyan függvényt, amely kiszámolja egy lista elemeinkek az átlagát.
10. Készíts egy függvényt ami beszúr egy element pont a lista közepére.
11. Készíts egy függvényt ami a lista minden elemét megszorozza 2-vel.
12. Készíts egy függvényt ami visszaadja a listát fordított sorrendben. (Ne a `reverse()` metódust használd. Írd meg a saját megoldásodat.)

# <div id="id-29"/> Megoldások
1. [Megoldás](solutions/1.py)
2. [Megoldás](solutions/2.py)
3. [Megoldás](solutions/3-4.py)
4. [Megoldás](solutions/3-4.py)
5. [Megoldás](solutions/5.py)
6. [Megoldás](solutions/6.py)
7. [Megoldás](solutions/7.py)
8. [Megoldás](solutions/8.py)
9. [Megoldás](solutions/9.py)
10. [Megoldás](solutions/10.py)
11. [Megoldás](solutions/11.py)
12. [Megoldás](solutions/12.py)

# <div id="id-30"/>Összefoglaló
- A listák olyan adatszerkezetek, amelyekben több elemet tudunk tárolni.
- A listák indexelhetőek, tehát hozzáférhetünk az elemekhez.
- A listák elemeit tudjuk módosítani.
- A listák elemeit tudjuk rendezni, megfordítani, eltávolítani, hozzáadni, beszúrni, másolni.
- A listák elemeit tudjuk összegezni, megszorozni, átlagát kiszámolni.
- A listák elemeit tudjuk ellenőrizni, hogy szerepelnek-e a listában és hogy hányszor szerepelnek.
- A listák elemeit tudjuk generálni és feltételes kifejezéseket használni.
- A listák elemeit tudjuk indexelni és szeletelni.
- A listák elemeit tudjuk más adatszerkezetekké alakítani.
- A listák elemeit tudjuk iterálni.
- A listák elemeit tudjuk másolni.
- A listák elemeit tudjuk összehasonlítani más listákkal.
- A listák elemeit tudjuk összehasonlítani más adatszerkezetekkel.
- A listák elemeit tudjuk ellenőrizni, hogy iterálhatóak-e.
