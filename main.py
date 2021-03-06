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
DISTRIBUER SUR LES DEUX FILES OK

"""
import random
from lib.libcard import Carte
from lib.libstack import Pile, File, Cellule
from window.window import window

# initializing the ui
window()

# defining the global variable
winner = False
paquet1 = None
paquet2 = None
pile1 = None
pile2 = None

# creating 52 cards packets


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

# Giving cards shuffled to both players


def distribuer(paquet):
    global paquet1
    global paquet2
    paquet = melange(paquet)
    paquet1 = File()
    paquet2 = File()
    print(f"{paquet}\n\n")
    for i in range(0, 52):
        if i % 2 == 0:
            paquet1.ajouter(paquet[i])
        else:
            paquet2.ajouter(paquet[i])
    return paquet1, paquet2

# shuffling cards with random module


def melange(t):
    random.shuffle(t)
    return t

# creating the stacks of cards


def pile_comparer_create():
    global pile1
    global pile2
    pile1 = Pile()
    pile2 = Pile()


# Comparing stacks to tell the winner


def pile_comparer():
    global pile1
    global pile2
    if pile1.est_vide() and pile2.est_vide():
        pile1.push(paquet1.retirer())
        pile2.push(paquet2.retirer())
        if pile1.contenu.valeur > pile2.contenu.valeur:
            print("le joueur 1 remporte la manche")
            # enlever les deux cartes mettre ds bon paquet
        elif pile2.contenu.valeur > pile1.contenu.valeur:
            print("le joueur 2 remporte la manche")
            # enlever les deux cartes mettre ds bon paquet
    else:
        print("bataille")
        pile1.push(paquet1.retirer())  # middle card
        pile2.push(paquet2.retirer())  # middle card
        pile1.push(paquet1.retirer())  # top card
        pile2.push(paquet2.retirer())  # top card
        # Si égalite : bataille on pioche une carte retournée puis une autre et on compare


paquet = createPaquet()
print(distribuer(paquet))
pile_comparer_create()
print(pile_comparer())

p = Pile()
p.push(1)
p.push(3)
print(len(p))
