"""
Vytvořte třídu pro číslo. Třída by měla mít následující funkce:

Hodnoty zápisu a čtení.
Převést číslo na oktální.
Převést číslo na hexadecimální.
Převést číslo na binární.
Vyzkoušejte všechny možnosti vytvořené třídy pomocí testování jednotek (nejmenovitě).

"""
import unittest


class Cislo:
    def __init__(self, hodnota):
        self.hodnota = hodnota

    def ziskej_hodnotu(self):
        return self.hodnota

    def nastav_hodnotu(self, nova_hodnota):
        self.hodnota = nova_hodnota

    def na_octalni(self):
        return oct(self.hodnota)

    def na_hexadecimalni(self):
        return hex(self.hodnota)

    def na_binarni(self):
        return bin(self.hodnota)


class TestCislo(unittest.TestCase):
    def setUp(self):
        self.cislo = Cislo(10)

    def test_ziskat_hodnotu(self):
        self.assertEqual(self.cislo.ziskej_hodnotu(), 10)

    def test_nastavit_hodnotu(self):
        self.cislo.nastav_hodnotu(20)
        self.assertEqual(self.cislo.ziskej_hodnotu(), 20)

    def test_na_octalni(self):
        self.assertEqual(self.cislo.na_octalni(), '0o12')

    def test_na_hexadecimalni(self):
        self.assertEqual(self.cislo.na_hexadecimalni(), '0xa')

    def test_na_binarni(self):
        self.assertEqual(self.cislo.na_binarni(), '0b1010')


if __name__ == '__main__':
    unittest.main()
