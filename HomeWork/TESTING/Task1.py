"""
Vytvořte třídu obsahující sadu celých čísel. Třída by měla mít následující funkce:

Součet prvků v sadě.
Aritmetický průměr prvků v sadě.
Maximální počet prvků v sadě.
Minimum prvků v sadě.
Vyzkoušejte všechny možnosti vytvořené třídy pomocí testování jednotek (nejmenovitě).

"""
import unittest


class SadaCisel:
    def __init__(self, prvky):
        self.prvky = prvky

    def soucet(self):
        return sum(self.prvky)

    def aritmeticky_prumer(self):
        return sum(self.prvky) / len(self.prvky) if self.prvky else 0

    def maximum(self):
        return max(self.prvky) if self.prvky else None

    def minimum(self):
        return min(self.prvky) if self.prvky else None


class TestSadaCisel(unittest.TestCase):
    def setUp(self):
        self.sada = SadaCisel([1, 2, 3, 4, 5])

    def test_soucet(self):
        self.assertEqual(self.sada.soucet(), 15)

    def test_aritmeticky_prumer(self):
        self.assertEqual(self.sada.aritmeticky_prumer(), 3.0)

    def test_maximum(self):
        self.assertEqual(self.sada.maximum(), 5)

    def test_minimum(self):
        self.assertEqual(self.sada.minimum(), 1)

    def test_empty_sada(self):
        empty_sada = SadaCisel([])
        self.assertEqual(empty_sada.soucet(), 0)
        self.assertEqual(empty_sada.aritmeticky_prumer(), 0)
        self.assertIsNone(empty_sada.maximum())
        self.assertIsNone(empty_sada.minimum())


if __name__ == '__main__':
    unittest.main()
