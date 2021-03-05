class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s


class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def ajouter(self, x):
        c = Cellule(x, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def __repr__(self):
        tab = []
        x = self.tete
        for i in range(26):
            if i != 25:
                tab.append(str(x.valeur))
                x = x.suivante
            else:
                tab.append(str(self.queue.valeur))
        return str(tab)


class Pile:
    def __init__(self):
        self.contenu = None

    def est_vide(self):

    def push(self):

    def pop(self):
