class Boty:
    def __init__(self, druh, typ, barva, cena, znacka, velikost):
        self.druh = druh
        self.typ = typ
        self.barva = barva
        self.cena = cena
        self.znacka = znacka
        self.velikost = velikost

    def __str__(self):
        return f'{self.znacka} {self.typ} ({self.barva}) - {self.druh}, Velikost: {self.velikost}, Cena: {self.cena} Kč'
