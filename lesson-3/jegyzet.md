<link href="../assets/styles/style_1.css" rel="stylesheet"/>

# Ma a listákkal fogunk tovább barátkozni és gyakorloni, illetve a halmazokkal ismerkedünk meg.


# <div id="Tartalomjegyzék"/> Tartalomjegyzék

1. [Halmazok](#Halmazok)
    1. [Operátorok](#Operátorok)
    2. [Metódusok](#Metódusok)
2. [Továbbiak](#Továbbiak)
    1. [for - else](#for-else)
    2. [all() és any()](#all()-és-any())
    3. [zip()](#zip())
    4. [enumerate()](#enumerate())
    5. [map()](#map())
    6. [filter()](#filter())
    7. [lambda](#lambda)
    8. [Fájlműveletek](#Fájlműveletek)
    9. [splitlines()](#splitlines)
3. [Feladatok](#Feladatok)
4. [Megoldások](#Megoldások)

# <div id="Halmazok"/> Halmazok

## <div id="Operátorok"/> Operátorok
- `|` unió
    - A két halmaz összes elemét tartalmazza
- `&` metszet
    - Azokat az elemeket tartalmazza, amelyek mindkét halmazban szerepelnek
- `-` különbség
    - Azokat az elemeket tartalmazza, amelyek az első halmazban szerepelnek, de a másodikban nem
- `^` szimmetrikus különbség
    - Azokat az elemeket tartalmazza, amelyek csak az egyik halmazban szerepelnek

## <div id="Metódusok"/> Metódusok
- `add(elem)`
    - Hozzáad egy elemet a halmazhoz
- `remove(elem)`
    - Eltávolít egy elemet a halmazból
- `pop()`
    - Egy elemet eltávolít a halmazból és visszaadja azt
- `clear()`
    - Törli a halmaz összes elemét
- `copy()`
    - Másolatot készít a halmazról
- `difference(halmaz)`
    - Visszaadja a halmaz és egy másik halmaz különbségét
- `intersection(halmaz)`
    - Visszaadja a halmaz és egy másik halmaz metszetét
- `union(halmaz)`  
    - Visszaadja a halmaz és egy másik halmaz unióját
- `symmetric_difference(halmaz)`
    - Visszaadja a halmaz és egy másik halmaz szimmetrikus különbségét
- `issubset(halmaz)`
    - Igazat ad vissza, ha a halmaz részhalmaza a másik halmaznak
- `issuperset(halmaz)`
    - Igazat ad vissza, ha a halmaz tartalmazza a másik halmazt
- `isdisjoint(halmaz)`
    - Igazat ad vissza, ha a két halmaznak nincs közös eleme

# <div id="Továbbiak"/> Továbbiak

## <div id="for-else"/> for - else
- A `for` ciklus után egy `else` ágat is írhatunk, amely akkor fut le, ha a ciklus nem szakadt meg `break` utasítással.
- Példa:
    ```python
    for i in range(5):
        print(i)
    else:
        print("A ciklus lefutott")
    ```
- Ez egy specifikusan pythonos dolog, amit más nyelvekben nem találunk meg.

## <div id="all()-és-any()"/> all() és any()
- `all(iterable)`
    - Igazat ad vissza, ha az összes elem igazat ad vissza
    - Képzeld el úgy, hogy egy `and` kapcsoló lenne az összes elem között
- `any(iterable)`
    - Igazat ad vissza, ha legalább egy elem igazat ad vissz
    - Képzeld el úgy, hogy egy `or` kapcsoló lenne az összes elem között

## <div id="zip()"/> zip()
- Egy vagy több iterálható objektumot összefűz
- Példa:
    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for x, y, z in zip(a, b, c):
        print(x, y, z)
    ```
    Ez a kód a következőt írja ki:
        ```
        1 4 7
        2 5 8
        3 6 9
        ```
    ```python
        zip(a, b, c) = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    ```
## <div id="enumerate()"/> enumerate()
- Egy iterálható objektumot felsorolja és a hozzá tartozó indexet is visszaadja
- Példa:
    ```python
    for i, elem in enumerate(["a", "b", "c"]):
        print(i, elem)
    ```
    Ez a kód a következőt írja ki:
        ```
        0 a
        1 b
        2 c
        ```
## <div id="map()"/> map()
- Egy függvényt alkalmaz egy iterálható objektum minden elemére
- Példa:
    ```python
    def f(x):
        return x ** 2
    print(list(map(f, [1, 2, 3])))
    ```
    Ez a kód a következőt írja ki:
        ```
        [1, 4, 9]
        ```
## <div id="filter()"/> filter()
- Egy függvényt alkalmaz egy iterálható objektum minden elemére, és csak azokat adja vissza, amelyekre a függvény igazat ad vissza
- Példa:
    ```python
    def f(x):
        return x % 2 == 0
    print(list(filter(f, [1, 2, 3, 4, 5, 6])))
    ```
    Ez a kód a következőt írja ki: `[2, 4, 6]`

## <div id="lambda"/> lambda
- Névtelen függvényeket hoz létre
- Ezek olyan függvények, amelyeket csak egyszer használunk, és nem akarunk nekik külön nevet adni
- Példa:
    ```python
    print((lambda x: x ** 2)(3))
    ```
    Ez a kód a következőt írja ki:`9`

## <div id="Fájlműveletek"/> Fájlműveletek
- Fájlok olvasása
    ```python
    with open("fájlnév", "r") as f: # A "r" jelzi, hogy olvasásra nyitjuk meg a fájlt (read)
        for sor in f:
            print(sor)
    ```
- Fájlok írása
    ```python
    with open("fájlnév", "w") as f: # A "w" jelzi, hogy írásra nyitjuk meg a fájlt (write)
        f.write("valami")
    ```
- Fájlok kiegészítése
    ```python
    with open("fájlnév", "a") as f: # A "a" jelzi, hogy kiegészítésre nyitjuk meg a fájlt (append)
        f.write("valami")
    ```
## <div id="splitlines"/> splitlines()
- A `splitlines()` metódus egy listát ad vissza, amelyben a fájl sorai szerepelnek
- Példa:
    ```python
    with open("fájlnév", "r") as f:
        sorok = f.read().splitlines()
    print(sorok)
    ```

- A fájlműveletek során a `with` kulcsszóval megnyitott fájl automatikusan bezáródik, amikor a blokk véget ér. Ez a fájlműveletek során nagyon fontos, mert ha nem zárjuk be a fájlt, akkor az operációs rendszer nem tudja, hogy a fájl már nem használatos, és nem tudja felszabadítani a memóriát, amit a fájl foglal.
- A nem `with` kulcsszóval megnyitott fájlt úgy lehet bezárni, hogy a `close()` metódust hívjuk meg rajta, de ez a módszer nem annyira biztonságos, mert ha a fájlműveletek során kivétel keletkezik, akkor a fájl nem fog bezáródni, és a memóriát fogja foglalni.
    - Példa:
        ```python
        f = open("fájlnév", "r")
        for sor in f:
            print(sor)
        f.close()
        ```

# <div id="Feladatok"/> Feladatok
1. Készítsünk egy függvényt, ami megkeresei az első olyan elemet egy listában, amelyik nem ismétlődik. Ha nincs ilyen, akkor adjon vissza egy `None` értéket.
2. Készítsünk egy függvényt, ami veszi két lista unióját, azaz az összes olyan elemet, ami legalább az egyik listában szerepel.
3. Készítsünk egy függvényt, ami veszi két lista metszetét, azaz az összes olyan elemet, ami mindkét listában szerepel.
4. Készítsünk egy függvényt, amely megvizsgálja egy listában található összes számot, és visszatér azzal, hogy minden szám pozitív-e vagy sem. 
5. Készítsünk egy függvényt, amely megvizsgálja egy listában található összes számot, és visszatér azzal, hogy legalább egy szám pozitív-e vagy sem.
6. Készítsünk egy függvényt, ami csak a páros számokat adja vissza egy listából.
7. Készítsünk egy függvényt, ami egy listában található összes számot négyzetre emel.
8. Készítsünk egy függvényt ami a listában található összes elem mögé hozzáfűz, hogy hányadik elemről van szó. Példa: `["a", "b", "c"]` -> `["1. a", "2. b", "3. c"]`
9. Készítsünk egy függvényt, ami egy fájlból beolvas egy listát, és visszaadja azt, és egy másik függvényt, ami egy listát kiír egy fájlba.


# <div id="Megoldások"/> Megoldások
1. [Megoldás](solutions/1.py)
2. [Megoldás](solutions/2.py)
3. [Megoldás](solutions/3.py)
4. [Megoldás](solutions/4.py)
5. [Megoldás](solutions/5.py)
6. [Megoldás](solutions/6.py)
7. [Megoldás](solutions/7.py)
8. [Megoldás](solutions/8.py)
9. [Megoldás](solutions/9.py)



[^^^](#Tartalomjegyzék)

