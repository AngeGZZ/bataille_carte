"""
14 : AS
13 : ROI
12 : DAME
11 : VALET
10
9
8
7
6
5
4
3
2

Si égalite : bataille on pioche une carte retournée puis une autre et on compare

CREATION PAQUET OK
MELANGE PAQUET OK
DISTRIBUER SUR LES DEUX FILES NO
"""

from tkinter import *
import random
from lib.libcard import *
from lib.libstack import *

fenetre = Tk()
fenetre.title("Bataille")
fenetre.config(bg="#87CEEB")
fenetre.geometry("1200x800")
fenetre.resizable(width=False, height=False)

winner = False


def createPaquet():
    paquet = []
    for i in range(2, 15):
        if (i <= 10):
            paquet.append(Carte(str(i), i, "pique"))
        elif (i == 11):
            paquet.append(Carte("Valet", i, "pique"))
        elif (i == 12):
            paquet.append(Carte("Dame", i, "pique"))
        elif (i == 13):
            paquet.append(Carte("Roi", i, "pique"))
        elif (i == 14):
            paquet.append(Carte("As", i, "pique"))
    for i in range(2, 15):
        if (i <= 10):
            paquet.append(Carte(str(i), i, "coeur"))
        elif (i == 11):
            paquet.append(Carte("Valet", i, "coeur"))
        elif (i == 12):
            paquet.append(Carte("Dame", i, "coeur"))
        elif (i == 13):
            paquet.append(Carte("Roi", i, "coeur"))
        elif (i == 14):
            paquet.append(Carte("As", i, "coeur"))
    for i in range(2, 15):
        if (i <= 10):
            paquet.append(Carte(str(i), i, "carreau"))
        elif (i == 11):
            paquet.append(Carte("Valet", i, "carreau"))
        elif (i == 12):
            paquet.append(Carte("Dame", i, "carreau"))
        elif (i == 13):
            paquet.append(Carte("Roi", i, "carreau"))
        elif (i == 14):
            paquet.append(Carte("As", i, "carreau"))
    for i in range(2, 15):
        if (i <= 10):
            paquet.append(Carte(str(i), i, "trefle"))
        elif (i == 11):
            paquet.append(Carte("Valet", i, "trefle"))
        elif (i == 12):
            paquet.append(Carte("Dame", i, "trefle"))
        elif (i == 13):
            paquet.append(Carte("Roi", i, "trefle"))
        elif (i == 14):
            paquet.append(Carte("As", i, "trefle"))
    return paquet


def distribuer(paquet):
    paquet = melange(paquet)
    paquet1 = File()
    paquet2 = File()
    print(f"{paquet}\n\n")
    for i in range(0, 52):
        if i % 2 == 0:
            paquet1.ajouter(paquet[i])
        else:
            paquet2.ajouter(paquet[i])
    return str(paquet1) + "\n\n" + str(paquet2)


def melange(t):
    random.shuffle(t)
    return t


paquet = createPaquet()
print(distribuer(paquet))
# fenetre.mainloop()
