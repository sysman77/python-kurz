class Clovek:
    def __init__(self, cele_jmeno, datum_narozeni, kontaktni_cislo, mesto, zeme, adresa_bydliste):
        self._cele_jmeno = cele_jmeno
        self._datum_narozeni = datum_narozeni
        self._kontaktni_cislo = kontaktni_cislo
        self._mesto = mesto
        self._zeme = zeme
        self._adresa_bydliste = adresa_bydliste
    
    # Metody pro vstup dat
    def set_cele_jmeno(self, cele_jmeno):
        self._cele_jmeno = cele_jmeno

    def set_datum_narozeni(self, datum_narozeni):
        self._datum_narozeni = datum_narozeni

    def set_kontaktni_cislo(self, kontaktni_cislo):
        self._kontaktni_cislo = kontaktni_cislo

    def set_mesto(self, mesto):
        self._mesto = mesto

    def set_zeme(self, zeme):
        self._zeme = zeme

    def set_adresa_bydliste(self, adresa_bydliste):
        self._adresa_bydliste = adresa_bydliste

    # Metody pro vystup dat
    def get_cele_jmeno(self):
        return self._cele_jmeno

    def get_datum_narozeni(self):
        return self._datum_narozeni

    def get_kontaktni_cislo(self):
        return self._kontaktni_cislo

    def get_mesto(self):
        return self._mesto

    def get_zeme(self):
        return self._zeme

    def get_adresa_bydliste(self):
        return self._adresa_bydliste

    # Metoda pro zobrazeni vsech informaci
    def zobrazit_informace(self):
        informace = (
            f"Cele jmeno: {self._cele_jmeno}\n"
            f"Datum narozeni: {self._datum_narozeni}\n"
            f"Kontaktni cislo: {self._kontaktni_cislo}\n"
            f"Mesto: {self._mesto}\n"
            f"Zeme: {self._zeme}\n"
            f"Adresa bydliste: {self._adresa_bydliste}\n"
        )
        return informace

# Vytvoreni instance tridy Clovek
clovek = Clovek("Jan Novak", "01.01.1990", "+420123456789", "Praha", "Ceska republika", "Namesti Svobody 1")

# Zobrazeni informaci
print(clovek.zobrazit_informace())

# Uprava a zobrazeni jednotlivych poli
clovek.set_mesto("Brno")
print("Nove mesto:", clovek.get_mesto())
