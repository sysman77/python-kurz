"""
Implementujte třídní knihu. Pole třídy by měly ukládat následující: název, rok vydání, vydavatel, žánr, autor, cena.
Implementujte metody tříd pro vstup a výstup dat, poskytněte přístup k jednotlivým polím prostřednictvím metod tříd.
"""

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    # Metoda pro nastavení názvu
    def set_title(self, title):
        self.title = title

    # Metoda pro získání názvu
    def get_title(self):
        return self.title

    # Metoda pro nastavení roku vydání
    def set_year(self, year):
        self.year = year

    # Metoda pro získání roku vydání
    def get_year(self):
        return self.year

    # Metoda pro nastavení vydavatele
    def set_publisher(self, publisher):
        self.publisher = publisher

    # Metoda pro získání vydavatele
    def get_publisher(self):
        return self.publisher

    # Metoda pro nastavení žánru
    def set_genre(self, genre):
        self.genre = genre

    # Metoda pro získání žánru
    def get_genre(self):
        return self.genre

    # Metoda pro nastavení autora
    def set_author(self, author):
        self.author = author

    # Metoda pro získání autora
    def get_author(self):
        return self.author

    # Metoda pro nastavení ceny
    def set_price(self, price):
        self.price = price

    # Metoda pro získání ceny
    def get_price(self):
        return self.price

    # Metoda pro výstup dat o knize
    def display_info(self):
        return (f"Title: {self.title}, Year: {self.year}, Publisher: {self.publisher}, "
                f"Genre: {self.genre}, Author: {self.author}, Price: {self.price}")

# Vytvoření instance třídy Book a ukázka použití metod
book1 = Book("R.U.R.", 1920, "Fortuna Libri", "SciFi", "Harper Lee", 99)

# Výstup dat o knize
print(book1.display_info())

# Nastavení nových hodnot
book1.set_title("Rychlé šípy")
book1.set_year(1938)
book1.set_publisher("Mladý hlasatel")
book1.set_genre("Komix")
book1.set_author("Jaroslav Foglar")
book1.set_price(799)

# Získání a tisk hodnot
print(book1.get_title())
print(book1.get_year())
print(book1.get_publisher())
print(book1.get_genre())
print(book1.get_author())
print(book1.get_price())

# Výstup dat o knize s novými hodnotami
print(book1.display_info())
