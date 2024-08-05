from abc import ABC, abstractmethod

# Model


class Pizza:
    def __init__(self, nazev, zakladni_cena):
        self.nazev = nazev
        self.zakladni_cena = zakladni_cena
        self.pridavky = []

    def pridat_pridavek(self, pridavek):
        self.pridavky.append(pridavek)

    def spocitat_cenu(self):
        return self.zakladni_cena + sum(pridavek.cena for pridavek in self.pridavky)

    def __str__(self):
        seznam_pridavku = ", ".join([pridavek.nazev for pridavek in self.pridavky])
        return f"{self.nazev} Pizza s {seznam_pridavku}. Celková cena: {self.spocitat_cenu():.2f} Kč"


class Pridavek:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena


class Objednavka:
    def __init__(self):
        self.pizzy = []
        self.zaplaceno = False

    def pridat_pizzu(self, pizza):
        self.pizzy.append(pizza)

    def spocitat_celkem(self):
        return sum(pizza.spocitat_cenu() for pizza in self.pizzy)

    def __str__(self):
        return "\n".join([str(pizza) for pizza in self.pizzy]) + f"\nCelkem: {self.spocitat_celkem():.2f} Kč"


class PlatbaStrategy(ABC):
    @abstractmethod
    def zaplatit(self, castka):
        pass


class PlatbaHotovosti(PlatbaStrategy):
    def zaplatit(self, castka):
        print(f"Zaplaceno {castka:.2f} Kč v hotovosti.")


class PlatbaKartou(PlatbaStrategy):
    def zaplatit(self, castka):
        print(f"Zaplaceno {castka:.2f} Kč kartou.")


class Prodeje:
    def __init__(self):
        self.celkove_prodeje = 0
        self.objednavky = []

    def zaznamenat_objednavku(self, objednavka):
        self.objednavky.append(objednavka)
        self.celkove_prodeje += objednavka.spocitat_celkem()

    def ziskat_souhrn_prodeju(self):
        return f"Celkové prodeje: {self.celkove_prodeje:.2f} Kč\nCelkový počet objednávek: {len(self.objednavky)}"


class SpravceSouboru:
    @staticmethod
    def ulozit_objednavku(objednavka, soubor='objednavky.json'):
        with open(soubor, 'a') as file:
            file.write(objednavka.__str__() + '\n')


class Parser:
    @staticmethod
    def parse_platba_metoda(metoda):
        if metoda.lower() == 'hotovost':
            return PlatbaHotovosti()
        elif metoda.lower() == 'karta':
            return PlatbaKartou()
        else:
            raise ValueError("Neznámá platební metoda")
