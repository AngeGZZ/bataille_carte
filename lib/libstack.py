class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

    def __repr__(self):
        return str(self.valeur)


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

    def retirer(self):
        if self.est_vide():
            raise IndexError("retirer File vide")
        x = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return x

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
        return self.contenu is None

    def push(self, x):
        c = Cellule(x, self.contenu)
        self.contenu = c

    def pop(self):
        if self.est_vide():
            raise IndexError("pop sur une pile vide")
        else:
            c = self.contenu.valeur
            self.contenu = self.contenu.suivante
        return c

    def __repr__(self):
        return self.contenu.valeur

    def __str__(self):
        return self.contenu.valeur

    def lenght(self, suivant=None):
        if not suivant:
            return 0
        else:
            return 1 + self.lenght(self.contenu.suivante)

    def __len__(self):
        if self.est_vide():
            return 0
        else:
            i = 1
            while self.contenu.suivante is not None:
                self.contenu = self.contenu.suivante
                i = i+1
            return i
