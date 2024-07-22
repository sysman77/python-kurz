from model import *

class BotyController:
    def __init__(self):
        self.boty_list = []
        self.kosik = Kosik()

    def pridat_boty(self, druh, typ, barva, cena, znacka, velikost):
        nove_boty = Boty(druh, typ, barva, cena, znacka, velikost)
        self.boty_list.append(nove_boty)
        return nove_boty

    def zobrazit_vsechny_boty(self):
        return self.boty_list

    def pridat_do_kosiku(self, boty):
        self.kosik.pridat_do_kosiku(boty)

    def odstran_z_kosiku(self, boty):
        self.kosik.odstranit_z_kosiku(boty)

    def zobrazit_kosik(self):
        return self.kosik.zobrazit_kosik()

    def zaplatit(self, metoda):
        pokladna = Pokladna(self.kosik)
        return pokladna.zaplatit(metoda)
