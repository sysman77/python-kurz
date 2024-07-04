import math

class Zlomek:
    def __init__(self, citatel, jmenovatel):
        if jmenovatel == 0:
            raise ValueError("Jmenovatel nemůže být nula.")
        self._citatel = citatel
        self._jmenovatel = jmenovatel
        self._zjednodusit()
    
    # Metody pro vstup dat
    def set_citatel(self, citatel):
        self._citatel = citatel
        self._zjednodusit()

    def set_jmenovatel(self, jmenovatel):
        if jmenovatel == 0:
            raise ValueError("Jmenovatel nemůže být nula.")
        self._jmenovatel = jmenovatel
        self._zjednodusit()

    # Metody pro výstup dat
    def get_citatel(self):
        return self._citatel

    def get_jmenovatel(self):
        return self._jmenovatel

    # Metoda pro zobrazení zlomku
    def zobrazit(self):
        return f"{self._citatel}/{self._jmenovatel}"
    
    # Metoda pro zjednodušení zlomku
    def _zjednodusit(self):
        delitel = math.gcd(self._citatel, self._jmenovatel)
        self._citatel //= delitel
        self._jmenovatel //= delitel

    # Aritmetické operace
    def __add__(self, other):
        citatel = self._citatel * other.get_jmenovatel() + other.get_citatel() * self._jmenovatel
        jmenovatel = self._jmenovatel * other.get_jmenovatel()
        return Zlomek(citatel, jmenovatel)

    def __sub__(self, other):
        citatel = self._citatel * other.get_jmenovatel() - other.get_citatel() * self._jmenovatel
        jmenovatel = self._jmenovatel * other.get_jmenovatel()
        return Zlomek(citatel, jmenovatel)

    def __mul__(self, other):
        citatel = self._citatel * other.get_citatel()
        jmenovatel = self._jmenovatel * other.get_jmenovatel()
        return Zlomek(citatel, jmenovatel)

    def __truediv__(self, other):
        if other.get_citatel() == 0:
            raise ValueError("Nelze dělit nulovým zlomkem.")
        citatel = self._citatel * other.get_jmenovatel()
        jmenovatel = self._jmenovatel * other.get_citatel()
        return Zlomek(citatel, jmenovatel)

# Příklady použití třídy Zlomek
z1 = Zlomek(1, 2)
z2 = Zlomek(3, 4)

print("Zlomek 1:", z1.zobrazit())
print("Zlomek 2:", z2.zobrazit())

z3 = z1 + z2
print("Součet:", z3.zobrazit())

z4 = z1 - z2
print("Rozdíl:", z4.zobrazit())

z5 = z1 * z2
print("Součin:", z5.zobrazit())

z6 = z1 / z2
print("Podíl:", z6.zobrazit())
