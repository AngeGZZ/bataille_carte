class Carte:
    def __init__(self, nom, valeur, couleur, visible=True):
        self.nom = nom
        self.valeur = valeur
        self.couleur = couleur
        self.visible = False

    def __str__(self):
        x = f"{self.nom} de {self.couleur}"
        return x

    def __repr__(self):
        x = f"{self.nom} de {self.couleur}"
        return x

    def __lt__(self, other):
        if self.valeur < other.valeur:
            return 0

    def __gt__(self, other):
        if self.valeur > other.valeur:
            return 1

    def __eq__(self, other):
        if self.valeur == other.valeur:
            return 2

    def retourne(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
