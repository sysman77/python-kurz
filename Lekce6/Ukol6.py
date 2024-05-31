def je_prestupny_rok(rok):

#  Funkce pro kontrolu, zda je rok přestupný.

  if rok % 4 != 0:
    return False
  elif rok % 100 == 0 and rok % 400 != 0:
    return False
  else:
    return True

def pocet_dni_v_mesici(mesic, rok): # Funkce pro výpočet počtu dnů v daném měsíci.

  if mesic in [4, 6, 9, 11]:
    return 30
  elif mesic == 2:
    if je_prestupny_rok(rok):
      return 29
    else:
      return 28
  else:
    return 31

def pocet_dni_mezi_daty(datum1, datum2): # Funkce pro výpočet počtu dnů mezi dvěma daty.

  rok1, mesic1, den1 = datum1.split("-")
  rok2, mesic2, den2 = datum2.split("-")

  pocet_dni = 0

  # Výpočet dnů zbývajících v roce 1
  pocet_dni += (365 - pocet_dni_v_mesici(int(mesic1), int(rok1))) - int(den1)

  # Výpočet dnů v celých letech mezi daty
  for rok in range(int(rok1) + 1, int(rok2)):
    if je_prestupny_rok(rok):
      pocet_dni += 366
    else:
      pocet_dni += 365

  # Výpočet dnů v roce 2
  for mesic in range(1, int(mesic2)):
    pocet_dni += pocet_dni_v_mesici(mesic, int(rok2))
  pocet_dni += int(den2)

  return pocet_dni

datum1 = "2020-01-01"
datum2 = "2024-05-24"

pocet_dni = pocet_dni_mezi_daty(datum1, datum2)
print(f"Počet dnů mezi {datum1} a {datum2}: {pocet_dni}")
