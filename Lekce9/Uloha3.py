class Zeme:
    def __init__(self, nazev_zeme, kontinent, populace, volaci_kod, hlavni_mesto, nazvy_mest):
        self._nazev_zeme = nazev_zeme
        self._kontinent = kontinent
        self._populace = populace
        self._volaci_kod = volaci_kod
        self._hlavni_mesto = hlavni_mesto
        self._nazvy_mest = nazvy_mest
    
    # Metody pro vstup dat
    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_kontinent(self, kontinent):
        self._kontinent = kontinent

    def set_populace(self, populace):
        self._populace = populace

    def set_volaci_kod(self, volaci_kod):
        self._volaci_kod = volaci_kod

    def set_hlavni_mesto(self, hlavni_mesto):
        self._hlavni_mesto = hlavni_mesto

    def set_nazvy_mest(self, nazvy_mest):
        self._nazvy_mest = nazvy_mest

    # Metody pro vystup dat
    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_kontinent(self):
        return self._kontinent

    def get_populace(self):
        return self._populace

    def get_volaci_kod(self):
        return self._volaci_kod

    def get_hlavni_mesto(self):
        return self._hlavni_mesto

    def get_nazvy_mest(self):
        return self._nazvy_mest

    # Metoda pro zobrazeni vsech informaci
    def zobrazit_informace(self):
        informace = (
            f"Nazev zeme: {self._nazev_zeme}\n"
            f"Kontinent: {self._kontinent}\n"
            f"Populace: {self._populace}\n"
            f"Volaci kod: {self._volaci_kod}\n"
            f"Hlavni mesto: {self._hlavni_mesto}\n"
            f"Nazvy mest: {', '.join(self._nazvy_mest)}\n"
        )
        return informace

# Vytvoreni instance tridy Zeme
zeme = Zeme("Ceska republika", "Evropa", 10700000, "+420", "Praha", ["Brno", "Ostrava", "Plzen", "Liberec"])

# Zobrazeni informaci
print(zeme.zobrazit_informace())

# Uprava a zobrazeni jednotlivych poli
zeme.set_nazev_zeme("Slovenska republika")
print("Nova zeme:", zeme.get_nazev_zeme())
