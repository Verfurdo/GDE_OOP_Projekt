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
            
    def elerheto_jaratok(self, datum):
        foglaltak = [f.jarat.jaratszam for f in self.foglalasok if f.datum.date() == datum.date()]
        return [j for j in self.jaratok if j.jaratszam not in foglaltak]


    def list_foglalasok(self):
        print(f"\nFoglalások – {self.nev}")
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

lt.foglalas("B101", datetime(2025, 6, 5), "Kiss József")
lt.foglalas("B101", datetime(2025, 6, 7), "Nagy Éva")
lt.foglalas("N201", datetime(2025, 5, 21), "Szabó László")
lt.foglalas("N201", datetime(2025, 6, 11), "Tóth Zsófia")
lt.foglalas("N401", datetime(2025, 5, 2), "Kovács Péter")
lt.foglalas("N401", datetime(2025, 6, 15), "Varga Anna")

# Felhasználói interfész
while True:
    szelesseg = 33
    print("=" * szelesseg)
    print(f"{'GDE-Tours':^{szelesseg}}")
    print(f"{'Repülőjegy Foglalási Rendszer':^{szelesseg}}")
    print(f"{'v1.2':^{szelesseg}}")
    print("=" * szelesseg)
    print("\nVálassz műveletet:")
    print("1. Jegy Foglalása")
    print("2. Foglalások listázása")
    print("3. Kilépés")
    valasztas = input("Művelet (1-3): ")


    if valasztas == "1":
        # Felhasználó nevének bekérése
        while True:
            nev = input("Add meg a neved: ").strip()
            if nev:
                break
            print("A név nem lehet üres!\n")

        #  Dátum bekérés
        while True:
            datum_str = input("Add meg a dátumot (ÉÉÉÉ.HH.NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y.%m.%d")
                if datum.date() < datetime.now().date():
                    print("Hibás dátum! Csak mai vagy jövőbeni dátum lehet.\n")
                else:
                    break
            except ValueError:
                print("Hibás dátum formátum! Pl. 2025.06.10\n")

        # Elérhető járatok lekérdezése
        jaratok = lt.elerheto_jaratok(datum)

        if not jaratok:
            print("Nincs elérhető járat ezen a napon.")
        else:
            print("\nElérhető járatok:")
            for i, j in enumerate(jaratok, 1):
                print(f"{i}. {j.jaratszam} -> {j.celallomas} ({j.jarat_tipus()}), Ár: {j.jegyar} Ft")

            # Járatválasztás
            try:
                val = int(input("Válassz járatot (sorszám): "))
                if 1 <= val <= len(jaratok):
                    kivalasztott_jarat = jaratok[val - 1]
                    lt.foglalas(kivalasztott_jarat.jaratszam, datum, nev)
                    print(f"\nSikeres foglalás, {nev.title()}! Ár: {kivalasztott_jarat.jegyar} Ft")
                else:
                    print("Hibás sorszám!")
            except ValueError:
                print("Hibás bevitel! Szám 1-5.")



    elif valasztas == "2":
        lt.list_foglalasok()
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
    elif valasztas == "3":
        print("Kilépés a programból...")
        break
    else:
        print("Csak 1-3!")
