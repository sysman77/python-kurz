from model import *
class BotyController:
    def __init__(self):
        self.boty_list = []

    def pridat_boty(self, druh, typ, barva, cena, znacka, velikost):
        nove_boty = Boty(druh, typ, barva, cena, znacka, velikost)
        self.boty_list.append(nove_boty)
        return nove_boty

    def zobrazit_vsechny_boty(self):
        return self.boty_list

    def najit_boty_podle_znacky(self, znacka):
        return [boty for boty in self.boty_list if boty.znacka == znacka]
