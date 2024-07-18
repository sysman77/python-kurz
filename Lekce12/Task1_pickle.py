import pickle

class Letadlo:
    def __init__(self, nazev, model, rok_vyroby, kapacita):
        self.nazev = nazev
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.kapacita = kapacita

    def info(self):
        return f"Letadlo: {self.nazev}, Model: {self.model}, Rok výroby: {self.rok_vyroby}, Kapacita: {self.kapacita}"

    def ulozit_do_souboru(self, soubor):
        with open(soubor, 'wb') as f:
            pickle.dump(self, f)
        print(f"Objekt byl úspěšně uložen do souboru {soubor}")

    @staticmethod
    def nacist_ze_souboru(soubor):
        with open(soubor, 'rb') as f:
            obj = pickle.load(f)
        print(f"Objekt byl úspěšně načten ze souboru {soubor}")
        return obj

# Příklad použití
letadlo1 = Letadlo("Boeing", "737", 1998, 150)
print(letadlo1.info())

# Uložit objekt do souboru
letadlo1.ulozit_do_souboru('letadlo.txt')

# Načíst objekt ze souboru
letadlo2 = Letadlo.nacist_ze_souboru('letadlo.txt')
print(letadlo2.info())
