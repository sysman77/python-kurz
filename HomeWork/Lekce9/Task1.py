"""
 Implementujte třídu Car. Pole třídy by měly ukládat následující: model, rok vydání, výrobce, objem motoru, barva, cena.
  Implementujte metody tříd pro vstup a výstup dat, poskytněte přístup k jednotlivým polím prostřednictvím metod tříd.

"""


class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    # Metoda pro nastavení modelu
    def set_model(self, model):
        self.model = model

    # Metoda pro získání modelu
    def get_model(self):
        return self.model

    # Metoda pro nastavení roku vydání
    def set_year(self, year):
        self.year = year

    # Metoda pro získání roku vydání
    def get_year(self):
        return self.year

    # Metoda pro nastavení výrobce
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    # Metoda pro získání výrobce
    def get_manufacturer(self):
        return self.manufacturer

    # Metoda pro nastavení objemu motoru
    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    # Metoda pro získání objemu motoru
    def get_engine_volume(self):
        return self.engine_volume

    # Metoda pro nastavení barvy
    def set_color(self, color):
        self.color = color

    # Metoda pro získání barvy
    def get_color(self):
        return self.color

    # Metoda pro nastavení ceny
    def set_price(self, price):
        self.price = price

    # Metoda pro získání ceny
    def get_price(self):
        return self.price

    # Metoda pro výstup dat o autě
    def display_info(self):
        return (f"Model: {self.model}, Year: {self.year}, Manufacturer: {self.manufacturer}, "
                f"Engine Volume: {self.engine_volume}, Color: {self.color}, Price: {self.price}")


# Vytvoření instance třídy Car a ukázka použití metod
car1 = Car("Kodiaq", 2022, "Škoda", 2.0, "červená", 1390000)

# Výstup dat o autě Kodiaq
print(car1.display_info())

# Nastavení nových hodnot
car1.set_model("Karoq")
car1.set_year(2020)
car1.set_manufacturer("Škoda")
car1.set_engine_volume(1.5)
car1.set_color("šedá")
car1.set_price(750000)

# Získání a tisk hodnot
print(car1.get_model())
print(car1.get_year())
print(car1.get_manufacturer())
print(car1.get_engine_volume())
print(car1.get_color())
print(car1.get_price())

# Výstup dat o autě Karoq
print(car1.display_info())
