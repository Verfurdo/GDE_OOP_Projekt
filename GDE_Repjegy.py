# Repülőjegy Foglalási Rendszer

# Alaposztály: Jarat
class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

class Belfoldi(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 15000)

class Nemzetkozi(Jarat):
    def __init__(self, jaratszam, celallomas, alap_ar):
        super().__init__(jaratszam, celallomas, alap_ar)

class Europa(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 45000)

class Amerika(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 85000)

class Azsia(Nemzetkozi):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 95000)
        
while True:
    print("\n--- AERO-GDE Repülőjegy Foglalási Rendszer ---")
    print("1. Új járat hozzáadása")
    print("2. Járatok listázása")
    print("3. Kilépés")

    valasztas = input("Választás (1/2/3): ")

    if valasztas == "1":
        jaratszam = input("Járatszám: ").strip().upper()
        cel = input("Célállomás: ").strip().title()
        print("Típus (1 = Belföldi, 2 = Európa, 3 = Amerika, 4 = Ázsia):")
        tipus = input("Típus választás: ")
        if tipus == "1":
            lt.add_jarat(Belfoldi(jaratszam, cel))
        elif tipus == "2":
            lt.add_jarat(Europa(jaratszam, cel))
        elif tipus == "3":
            lt.add_jarat(Amerika(jaratszam, cel))
        elif tipus == "4":
            lt.add_jarat(Azsia(jaratszam, cel))
        else:
            print("Ismeretlen típus.")
    elif valasztas == "2":
        if not lt.jaratok:
            print("Nincs elérhető járat.")
        else:
            print("\nElérhető járatok:")
            for j in lt.jaratok:
                print(f"{j.jaratszam} -> {j.celallomas}, {j.jegyar} Ft")
    elif valasztas == "3":
        print("Kilépés...")
        break
    else:
        print("Hibás választás!")
