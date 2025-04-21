# GDE_OOP_Projekt

✈️ GDE-Tours – Repülőjegy Foglalási Rendszer
Ez a Python-alapú alkalmazás egy repülőjegy-foglalási rendszert valósít meg konzolos felhasználói felületen keresztül. 

Funkciók
✅ Belföldi és nemzetközi járatok kezelése
✅ Jegyfoglalás megadott dátumra és névre
✅ Foglalások listázása
✅ Foglalás lemondása
✅ Alapértelmezett járatok és foglalások betöltése


Projekt felépítése:

A rendszer osztály-alapú megközelítéssel működik:
Jarat – absztrakt osztály
Belfoldi, Europa, Amerika, Azsia – származtatott osztályok - konkrét járattípusok
JegyFoglalas – foglalás adatait tárolja
LegiTarsasag – járatok és foglalások kezelése

Használat:
Futtatás
python GDE_Repjegy.py


Menüpontok:

1 – Jegy foglalása (név, dátum, járat kiválasztása)
2 – Foglalás lemondása (név alapú foglalás lemondás)
3 – Összes foglalás megtekintése
4 – Kilépés


📅 Felhasználói interfész:

=================================
           GDE-Tours
   Repülőjegy Foglalási Rendszer
              v1.x
=================================

Válassz műveletet:
1. Jegy Foglalása
2. Foglalas Lemondása
3. Foglalások Listázása
4. Kilépés


⚠️ Követelmények

Python 3.7+
Nincs külső csomag, csak beépített Python modulokat használ