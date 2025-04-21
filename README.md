# GDE OOP PROJEKT
# GDE-Tours – Repülőjegy Foglalási Rendszer

Egy konzolos repülőjegy foglalási rendszer Pythonban. A program lehetőséget nyújt belföldi és nemzetközi járatok kezelésére, valamint jegyfoglalásra, lemondásra és foglalások listázására.

## Tartalom

- [Előfeltételek](#elofeltetelek)
- [Telepítés](#telepites)
- [Használat](#hasznalat)
- [Fájlok magyarázata](#fajlok-magyarazata)
- [Működés](#mukodes)
- [Közreműködők](#kozremukodok)

## Előfeltételek

A projekt kizárólag beépített Python modulokat használ, nincs szükség külön telepítésre:
•	datetime
•	os
•	abc

Python 3.7 vagy újabb ajánlott.

## Telepítés

1.	Klónozd vagy töltsd le a projektet:
	git clone https://github.com/Verfurdo/GDE_OOP_Projekt

2.	Futtasd a fő programot:
	python GDE_Repjegy.py

## Használat

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

Indítás után egy konzolos menü jelenik meg, ahol a következő opciók közül választhatsz:
•	1 – Jegy Foglalása: Add meg a neved, a dátumot, majd válassz egy elérhető járatot.
•	2 – Foglalás Lemondása: Válaszd ki saját foglalásaid közül, melyiket szeretnéd törölni.
•	3 – Foglalások Listázása: Az összes foglalás megtekintése.
•	4 – Kilépés: A program bezárása.

## Fájlok magyarázata

•	GDE_Repjegy.py: A teljes program logikáját és konzolos kezelőfelületét tartalmazza.
	o	Jarat: Absztrakt alaposztály járatokhoz.
	o	Belfoldi / Europa / Amerika / Azsia: Származtatott osztályok - Konkrét járattípusok.
	o	JegyFoglalas: Foglalás adatait tárolja (járat, dátum, név).
	o	LegiTarsasag: Kezeli a járatokat és foglalásokat.
	
## Működés
A program elindulásakor a GDE-TOURS légitársaság előre feltöltött járatlistával és foglalásokkal rendelkezik. A felhasználó a menüben foglalhat jegyet, lekérdezheti vagy lemondhatja saját foglalásait.
A rendszer a dátum alapján ellenőrzi az elérhető járatokat. Minden foglalás egy JegyFoglalas objektumként kerül eltárolásra, ami tartalmazza a járat adatait, a foglalás dátumát és a felhasználó nevét.

## Közreműködők

-   [VérFürdő]