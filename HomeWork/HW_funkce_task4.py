def najdi_nejmensi(cislo1, cislo2, cislo3, cislo4, cislo5):

  # Inicializace proměnné pro nejmenší číslo
  nejmensi = cislo1

  # Procházení zadaných čísel a nalezení nejmenšího
  for cislo in [cislo2, cislo3, cislo4, cislo5]:
    if cislo < nejmensi:
      nejmensi = cislo

  # Vrácení nejmenšího čísla
  return nejmensi

nejmensi_cislo = najdi_nejmensi(10, 5, 2, 4, 1)
print(f"Nejmenší číslo je: {nejmensi_cislo}")