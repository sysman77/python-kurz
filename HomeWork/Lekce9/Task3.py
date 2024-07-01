"""
Implementujte třídu Stadium. Pole třídy ukládají následující údaje: název stadionu, datum otevření, země, město, počet
míst k sezení. Implementujte metody třídy pro vstup a výstup dat, poskytněte přístup k jednotlivým polím
prostřednictvím metod třídy.
"""

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    # Metoda pro nastavení názvu stadionu
    def set_name(self, name):
        self.name = name

    # Metoda pro získání názvu stadionu
    def get_name(self):
        return self.name

    # Metoda pro nastavení data otevření
    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    # Metoda pro získání data otevření
    def get_opening_date(self):
        return self.opening_date

    # Metoda pro nastavení země
    def set_country(self, country):
        self.country = country

    # Metoda pro získání země
    def get_country(self):
        return self.country

    # Metoda pro nastavení města
    def set_city(self, city):
        self.city = city

    # Metoda pro získání města
    def get_city(self):
        return self.city

    # Metoda pro nastavení kapacity
    def set_capacity(self, capacity):
        self.capacity = capacity

    # Metoda pro získání kapacity
    def get_capacity(self):
        return self.capacity

    # Metoda pro výstup dat o stadionu
    def display_info(self):
        return (f"Name: {self.name}, Opening Date: {self.opening_date}, Country: {self.country}, "
                f"City: {self.city}, Capacity: {self.capacity}")

# Vytvoření instance třídy Stadium a ukázka použití metod
stadium1 = Stadium("Camp Nou", "24.9. 1957", "Spain", "Barcelona", 99354)

# Výstup dat o stadionu
print(stadium1.display_info())

# Nastavení nových hodnot
stadium1.set_name("Wembley Stadium")
stadium1.set_opening_date("9.3. 2007")
stadium1.set_country("United Kingdom")
stadium1.set_city("London")
stadium1.set_capacity(90000)

# Získání a tisk hodnot
print(stadium1.get_name())
print(stadium1.get_opening_date())
print(stadium1.get_country())
print(stadium1.get_city())
print(stadium1.get_capacity())

# Výstup nových dat o stadionu
print(stadium1.display_info())
