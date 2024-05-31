def zobraz_suda_cisla(cislo1, cislo2):

  # Kontrola pořadí čísel
  if cislo1 > cislo2:
    cislo1, cislo2 = cislo2, cislo1

  # Zobrazení sudých čísel v rozmezí
  print(f"Sudá čísla v rozmezí {cislo1} až {cislo2}:")
  for cislo in range(cislo1, cislo2 + 1, 2):
    print(cislo)

zobraz_suda_cisla(10, 20)

