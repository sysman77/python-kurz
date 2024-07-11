import pickle
import json

class Letadlo:
    def __init__(self, nazev, model, rok_vyroby, kapacita):
        self.nazev = nazev
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.kapacita = kapacita

    def info(self):
        return f"Letadlo: {self.nazev}, Model: {self.model}, Rok výroby: {self.rok_vyroby}, Kapacita: {self.kapacita}"

    def ulozit_do_souboru_pickle(self, soubor):
        with open(soubor, 'wb') as f:
            pickle.dump(self, f)
        print(f"Objekt byl úspěšně uložen do souboru {soubor} pomocí Pickle")

    @staticmethod
    def nacist_ze_souboru_pickle(soubor):
        with open(soubor, 'rb') as f:
            obj = pickle.load(f)
        print(f"Objekt byl úspěšně načten ze souboru {soubor} pomocí Pickle")
        return obj

    def ulozit_do_souboru_json(self, soubor):
        with open(soubor, 'w') as f:
            json.dump(self.__dict__, f)
        print(f"Objekt byl úspěšně uložen do souboru {soubor} pomocí JSON")

    @staticmethod
    def nacist_ze_souboru_json(soubor):
        with open(soubor, 'r') as f:
            data = json.load(f)
        obj = Letadlo(**data)
        print(f"Objekt byl úspěšně načten ze souboru {soubor} pomocí JSON")
        return obj

# Příklad použití
letadlo1 = Letadlo("Boeing", "737", 1998, 150)
print(letadlo1.info())

# Uložit objekt do souboru pomocí Pickle
letadlo1.ulozit_do_souboru_pickle('letadlo.txt')

# Načíst objekt ze souboru pomocí Pickle
letadlo2 = Letadlo.nacist_ze_souboru_pickle('letadlo.txt')
print(letadlo2.info())

# Uložit objekt do souboru pomocí JSON
letadlo1.ulozit_do_souboru_json('letadlo.json')

# Načíst objekt ze souboru pomocí JSON
letadlo3 = Letadlo.nacist_ze_souboru_json('letadlo.json')
print(letadlo3.info())
