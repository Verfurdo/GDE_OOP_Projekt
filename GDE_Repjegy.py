# Repülőjegy Foglalási Rendszer

from abc import ABC, abstractmethod
from datetime import datetime
import os
import time

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

    def lemondas(self, jaratszam, datum, felhasznalo):
        for f in self.foglalasok:
            if f.jarat.jaratszam == jaratszam and f.datum == datum and f.felhasznalo == felhasznalo:
                self.foglalasok.remove(f)
                return True
        return False
    
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
        
def torol_konzol():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kozepre(szoveg, szelesseg=60, karakter=" "):
    return szoveg.center(szelesseg, karakter)

def cian(szoveg):
    return "\033[36m" + szoveg + "\033[0m"

def bejelentkezes():
    print("=" * 50)
    print("|{:^48}|".format("GDE-Tours"))
    print("|{:^48}|".format("Bejelentkezési Felület"))
    print("=" * 50)
    
    while True:
        nev = input("Add meg a neved a bejelentkezéshez: ")
        if nev.strip():
            break
        print("A név nem lehet üres!\n")
        
    print("\nÜdvözöllek {}! Sikeres bejelentkezés...".format(nev))
    time.sleep(2)
    return nev


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

# Felhasználó nevének bekérése
nev = bejelentkezes()

# Menüpontok        
while True:
    torol_konzol()
    szelesseg = 60
    print("=" * szelesseg)
    print(cian(kozepre("GDE-Tours")))
    print(cian(kozepre("Repülőjegy Foglalási Rendszer")))
    print(cian(kozepre("v2.0")))
    print("=" * szelesseg)
    print(cian(kozepre(f"Bejelentkezve: {nev}")))
    print("=" * szelesseg)
    print("\n" + (cian(kozepre("Menüpontok:\n"))))
    print(cian(kozepre("1. Jegy Foglalása")))
    print(cian(kozepre("2. Foglalás Lemondása")))
    print(cian(kozepre("3. Foglalások Listázása")))
    print(cian(kozepre("4. Kilépés")))
    print("=" * szelesseg)
    valasztas = input(" Válassz a menüpontok közül (1-4): ")


    if valasztas == "1":
        while True:
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
                    print("Hibás dátum formátum (ÉÉÉÉ.HH.NN)\n")

            # Elérhető járatok lekérdezése
            jaratok = lt.elerheto_jaratok(datum)

            if not jaratok:
                print("Nincs elérhető járat ezen a napon.")
            else:
                print("\nElérhető járatok:")
                for i, j in enumerate(jaratok, 1):
                    print(f"{i}. {j.jaratszam} -> {j.celallomas} ({j.jarat_tipus()}), Ár: {j.jegyar} Ft")

                # Járatválasztás
                while True:
                    try:
                        val = int(input("Válassz járatot (sorszám): "))
                        if 1 <= val <= len(jaratok):
                            kivalasztott_jarat = jaratok[val - 1]
                            lt.foglalas(kivalasztott_jarat.jaratszam, datum, nev)
                            print(f"\nSikeres foglalás, {nev.title()}! Ár: {kivalasztott_jarat.jegyar} Ft")
                            break
                        else:
                            print("Hibás sorszám! Próbáld újra.\n")
                    except ValueError:
                        print("Hibás bevitel! Csak sorszámot írj be.\n")
            input("\nA folytatáshoz nyomd meg az ENTER gombot...")

            ujra = input("Szeretnél még foglalást? (i/n): ").strip().lower()
            if ujra != "i":
                break

    elif valasztas == "2":
        while True:            
            print("A te foglalásaid:")
            sajat_foglalasok = [f for f in lt.foglalasok if f.felhasznalo == nev]
            if not sajat_foglalasok:
                print("Nincs lemondható foglalásod.")
                input("\n A folytatáshoz nyomd meg az ENTER gombot...")
                break
            for idx, f in enumerate(sajat_foglalasok, 1):
                print(f"{idx}. Járat: {f.jarat.jaratszam}, Cél: {f.jarat.celallomas}, Dátum: {f.datum.strftime('%Y.%m.%d')}, Ár: {f.jarat.jegyar} Ft")

            while True:
                val = input("Add meg a lemondandó foglalás sorszámát: ")
                if val.isdigit() and (1 <= int(val) <= len(sajat_foglalasok)):
                    break
                print("Hibás sorszám! Kérlek, próbáld újra.")
                
            kivalasztott = sajat_foglalasok[int(val)-1]
            jaratszam = kivalasztott.jarat.jaratszam
            datum = kivalasztott.datum
            if lt.lemondas(jaratszam, datum, nev):
                    print("Foglalás lemondva.")
                    input("\n A folytatáshoz nyomd meg az ENTER gombot...")

            else:
                    print("Nincs ilyen foglalás vagy nem a te foglalásod.")
                    input("\n A folytatáshoz nyomd meg az ENTER gombot...")
                    
            ujra = input("Szeretnél másik foglalást is lemondani? (i/n): ").lower()
            if ujra != "i":
                break
        
    elif valasztas == "3":
        lt.list_foglalasok()
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
        
    elif valasztas == "4":
        print("Kilépés a programból...")
        break
    else:
        print("Csak 1-4!")
