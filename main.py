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
"""

from tkinter import *
import random

fenetre = Tk()
fenetre.title("Bataille")
fenetre.config(bg="#87CEEB")
fenetre.geometry("1200x800")
fenetre.resizable(width=False, height=False)

winner = False


class Carte:
    def __init__(self, nom, valeur, couleur):
        self.nom = nom
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        x = f"{self.nom} de {self.couleur}"
        return x

    def __repr__(self):
        x = f"{self.nom} de {self.couleur}"
        return x

    def compare(self, other):
        if self.valeur < other.valeur:
            return 0
        elif other.valeur < self.valeur:
            return 1
        else:
            return 2


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


def melange(t):
    random.shuffle(t)
    return t


x = createPaquet()
print(x)
#y = Carte("As", 14, "coeur")
# print(y)
print("-----------------------------")
y = melange(x)
print(y)

carte1 = Carte("As", 14, "carreau")
print(carte1)
carte2 = Carte("10", 10, "coeur")
print(carte1.compare(carte2))
"""
CREATION PAQUET OK
MELANGE PAQUET OK
DISTRIBUER SUR LES DEUX FILES NO



"""
"""
# distribuer

# paquetA
paquetB
"""
