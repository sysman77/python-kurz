# Model pro boty
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


# Model pro košík
class Kosik:
    def __init__(self):
        self.items = []

    def pridat_do_kosiku(self, boty):
        self.items.append(boty)

    def odstranit_z_kosiku(self, boty):
        self.items.remove(boty)

    def celkovy_cena(self):
        return sum(boty.cena for boty in self.items)

    def zobrazit_kosik(self):
        return self.items

    def vymazat_kosik(self):
        self.items.clear()


# Model pro pokladnu
class Pokladna:
    def __init__(self, kosik):
        self.kosik = kosik

    def zaplatit(self, metoda):
        celkova_cena = self.kosik.celkovy_cena()
        if metoda == 'hotově':
            self.kosik.vymazat_kosik() # Vymazání košíku po platbě
            return f'Úspěšně zaplaceno {celkova_cena} Kč hotově. Košík je prázdný'
        elif metoda == 'kartou':
            self.kosik.vymazat_kosik() # Vymazání košíku po platbě
            return f'Úspěšně zaplaceno {celkova_cena} Kč kartou. Košík je prázdný'
        else:
            return 'Neplatná metoda platby.'


