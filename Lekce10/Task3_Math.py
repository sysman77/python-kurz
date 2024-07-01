"""
Vytvořte třídu pro nalezení největšího a nejmenšího ze čtyř argumentů, průměru a faktoriálu.
Implementujte tuto funkci jako statické metody.
"""

import math

class MatematickéFunkce:
    @staticmethod
    def najdi_max(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def najdi_min(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def vypocitej_prumer(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def vypocitej_faktorial(n):
        if n < 0:
            raise ValueError("Faktoriál není definován pro záporná čísla")
        return math.factorial(n)

# Příklady použití:
max_hodnota = MatematickéFunkce.najdi_max(10, 20, 30, 40)
min_hodnota = MatematickéFunkce.najdi_min(10, 20, 30, 40)
prumer_hodnota = MatematickéFunkce.vypocitej_prumer(10, 20, 30, 40)
faktorial_hodnota = MatematickéFunkce.vypocitej_faktorial(5)

# Výpis výsledků
print(f"Největší hodnota: {max_hodnota}")
print(f"Nejmenší hodnota: {min_hodnota}")
print(f"Průměr: {prumer_hodnota}")
print(f"Faktoriál: {faktorial_hodnota}")

"""
V tomto kódu:

Třída MatematickéFunkce obsahuje čtyři statické metody.
najdi_max(a, b, c, d) vrací největší z hodnot a, b, c a d pomocí vestavěné funkce max().
najdi_min(a, b, c, d) vrací nejmenší z hodnot a, b, c a d pomocí vestavěné funkce min().
vypocitej_prumer(a, b, c, d) vrací průměr hodnot a, b, c a d.
vypocitej_faktorial(n) vrací faktoriál čísla n pomocí funkce math.factorial() a kontroluje, zda je n nezáporné.
Tímto způsobem můžete pomocí statických metod třídy MatematickéFunkce snadno provádět požadované matematické operace.
"""