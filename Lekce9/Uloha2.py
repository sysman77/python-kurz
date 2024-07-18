class Mesto:
    def __init__(self, nazev_mesta, nazev_regionu, nazev_zeme, pocet_obcanu, psc, predcisli):
        self._nazev_mesta = nazev_mesta
        self._nazev_regionu = nazev_regionu
        self._nazev_zeme = nazev_zeme
        self._pocet_obcanu = pocet_obcanu
        self._psc = psc
        self._predcisli = predcisli
    
    # Metody pro vstup dat
    def set_nazev_mesta(self, nazev_mesta):
        self._nazev_mesta = nazev_mesta

    def set_nazev_regionu(self, nazev_regionu):
        self._nazev_regionu = nazev_regionu

    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_pocet_obcanu(self, pocet_obcanu):
        self._pocet_obcanu = pocet_obcanu

    def set_psc(self, psc):
        self._psc = psc

    def set_predcisli(self, predcisli):
        self._predcisli = predcisli

    # Metody pro vystup dat
    def get_nazev_mesta(self):
        return self._nazev_mesta

    def get_nazev_regionu(self):
        return self._nazev_regionu

    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_pocet_obcanu(self):
        return self._pocet_obcanu

    def get_psc(self):
        return self._psc

    def get_predcisli(self):
        return self._predcisli

    # Metoda pro zobrazeni vsech informaci
    def zobrazit_informace(self):
        informace = (
            f"Nazev mesta: {self._nazev_mesta}\n"
            f"Nazev regionu: {self._nazev_regionu}\n"
            f"Nazev zeme: {self._nazev_zeme}\n"
            f"Pocet obcanu: {self._pocet_obcanu}\n"
            f"PSC: {self._psc}\n"
            f"Predcisli: {self._predcisli}\n"
        )
        return informace

# Vytvoreni instance tridy Mesto
mesto = Mesto("Praha", "Hlavni mesto", "Ceska republika", 1300000, "11000", "+420")

# Zobrazeni informaci
print(mesto.zobrazit_informace())

# Uprava a zobrazeni jednotlivych poli
mesto.set_nazev_mesta("Brno")
print("Nove mesto:", mesto.get_nazev_mesta())
