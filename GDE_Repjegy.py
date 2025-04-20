# Repülőjegy Foglalási Rendszer

from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt osztály: Jarat
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.orszag = self.get_orszag(celallomas)

    def get_orszag(self, varos):
        orszagok = {
            "Debrecen": "Magyarország",
            "Szeged": "Magyarország",
            "London": "Anglia",
            "New York": "USA",
            "Tokió": "Japán"
        }
        return orszagok.get(varos, "Ismeretlen")

    @abstractmethod
    def jarat_tipus(self):
        pass

# Származtatott osztályok
class Belfoldi(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 15000)

    def jarat_tipus(self):
        return "Belföldi járat"

class Nemzetkozi(Jarat):
    def __init__(self, jaratszam, celallomas, alap_ar):
        super().__init__(jaratszam, celallomas, alap_ar)

    def jarat_tipus(self):
        return "Nemzetközi járat"

class Europa(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 45000)

class Amerika(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 85000)

class Azsia(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 95000)

# JegyFoglalas osztály
class JegyFoglalas:
    def __init__(self, jarat, datum, felhasznalo):
        self.jarat = jarat
        self.datum = datum
        self.felhasznalo = felhasznalo

# Légitársaság osztály
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

    def foglalas(self, jaratszam, datum, felhasznalo):
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                self.foglalasok.append(JegyFoglalas(j, datum, felhasznalo))
                return

    def list_foglalasok(self):
        print(f"\nJelenlegi foglalások – {self.nev}")
        if not self.foglalasok:
            print("Nincsenek foglalások.")
            return

        print("-" * 65)
        print(f"{'Név':<20} | {'Járat':<6} | {'Dátum':^12} | {'Ár':^10}")
        print("-" * 65)
        for f in self.foglalasok:
            nev = f.felhasznalo.title()
            jarat = f.jarat.jaratszam
            datum = f.datum.strftime('%Y-%m-%d')
            ar = f"{f.jarat.jegyar} Ft"
            print(f"{nev:<20} | {jarat:<6} | {datum:<12} | {ar:>10}")
        print("-" * 65)

# Előre felvitt adatok
lt = LegiTarsasag("GDE-TOURS")

lt.add_jarat(Belfoldi("B101", "Debrecen"))
lt.add_jarat(Belfoldi("B102", "Szeged"))
lt.add_jarat(Europa("N201", "London"))
lt.add_jarat(Amerika("N301", "New York"))
lt.add_jarat(Azsia("N401", "Tokió"))

lt.foglalas("B101", datetime(2024, 6, 5), "Kiss József")
lt.foglalas("B101", datetime(2024, 6, 7), "Nagy Éva")
lt.foglalas("N201", datetime(2025, 5, 21), "Szabó László")
lt.foglalas("N201", datetime(2024, 6, 11), "Tóth Zsófia")
lt.foglalas("N401", datetime(2025, 5, 2), "Kovács Péter")
lt.foglalas("N401", datetime(2024, 6, 15), "Varga Anna")

# Felhasználói interfész
while True:
    szelesseg = 33
    print("=" * szelesseg)
    print(f"{'GDE-Tours':^{szelesseg}}")
    print(f"{'Repülőjegy Foglalási Rendszer':^{szelesseg}}")
    print(f"{'v1.0':^{szelesseg}}")
    print("=" * szelesseg)
    print("\nVálassz műveletet:")
    print("1. Foglalások listázása")
    print("2. Kilépés")
    valasztas = input("Művelet (1-2): ")

    if valasztas == "1":
        lt.list_foglalasok()
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
    elif valasztas == "2":
        print("Kilépés a programból...")
        break
    else:
        print("Csak 1 vagy 2!")
