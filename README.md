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
-	datetime
-	os
-	abc

Python 3.7 vagy újabb ajánlott.

## Telepítés

1.	Klónozd vagy töltsd le a projektet:
	git clone https://github.com/Verfurdo/GDE_OOP_Projekt

2.	Futtasd a fő programot:
	python GDE_Repjegy.py

## Használat

Indítás után egy konzolos menü jelenik meg, ahol a következő opciók közül választhatsz:
-	1 – Jegy Foglalása: Add meg a neved, a dátumot, majd válassz egy elérhető járatot.
-	2 – Foglalás Lemondása: Válaszd ki saját foglalásaid közül, melyiket szeretnéd törölni.
-	3 – Foglalások Listázása: Az összes foglalás megtekintése.
-	4 – Kilépés: A program bezárása.

## Fájlok magyarázata

-	GDE_Repjegy.py: A teljes program logikáját és konzolos kezelőfelületét tartalmazza.
	-	Jarat: Absztrakt alaposztály járatokhoz.
	-	Belfoldi / Europa / Amerika / Azsia: Származtatott osztályok - Konkrét járattípusok.
	-	JegyFoglalas: Foglalás adatait tárolja (járat, dátum, név).
	-	LegiTarsasag: Kezeli a járatokat és foglalásokat.
	
## Működés
A program elindulásakor a GDE-TOURS légitársaság előre feltöltött járatlistával és foglalásokkal rendelkezik. A felhasználó a menüben foglalhat jegyet, lekérdezheti vagy lemondhatja saját foglalásait.
A rendszer a dátum alapján ellenőrzi az elérhető járatokat. Minden foglalás egy JegyFoglalas objektumként kerül eltárolásra, ami tartalmazza a járat adatait, a foglalás dátumát és a felhasználó nevét.

## Közreműködők

-   [VérFürdő]