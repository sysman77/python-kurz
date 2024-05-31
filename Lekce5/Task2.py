"""
def zobraz_licha_cisla(cislo1, cislo2):
  
  Tato funkce vezme dvě čísla jako parametry a zobrazí všechna lichá čísla mezi nimi.

  Argumenty:
    cislo1: První číslo v rozsahu.
    cislo2: Druhé číslo v rozsahu.

  Příklad použití:
    zobraz_licha_cisla(5, 15)
  

  for i in range(cislo1,cislo2):
        if i % 2 == 1:
            print(i)

            # Příklad použití
zobraz_licha_cisla(5, 15)

"""


def zobraz_licha_cisla(cislo1, cislo2):
  """
  Tato funkce vezme dvě čísla jako parametry a zobrazí všechna lichá čísla mezi nimi.

  Argumenty:
    cislo1: První číslo v rozsahu.
    cislo2: Druhé číslo v rozsahu.

  Příklad použití:
    zobraz_licha_cisla(5, 15)
  """

  if cislo1 > cislo2:
    # Pokud je první číslo větší než druhé, prohodíme je.
    cislo1, cislo2 = cislo2, cislo1

  for cislo in range(cislo1, cislo2 + 1, 2):
    print(cislo)

# Příklad použití
zobraz_licha_cisla(5, 15)

