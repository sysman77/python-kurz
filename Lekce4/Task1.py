from random import randint

# Vytvoření seznamu náhodných čísel
seznam = [randint(-10, 10) for _ in range(10)]

# Inicializace proměnných pro součty a součiny
soucet_zapornych = 0
soucet_suchych = 0
soucet_lichych = 0
soucin_3_index = 1
soucin_min_max = 1
soucet_kladne = 0

# Procházení seznamu a sčítání/násobení
min_cislo = max_cislo = seznam[0]
prvni_kladne = None
posledni_kladne = None
for i, cislo in enumerate(seznam):
  if cislo < 0:
    soucet_zapornych += cislo
  elif cislo % 2 == 0:
    soucet_suchych += cislo
  else:
    soucet_lichych += cislo

  # Součin prvků s indexy dělitelnými 3
  if i % 3 == 0:
    soucin_3_index *= cislo

  # Součin prvků mezi nejmenším a největším prvkem
  if cislo < min_cislo:
    min_cislo = cislo
  elif cislo > max_cislo:
    max_cislo = cislo
  if cislo > 0:
    if prvni_kladne is None:
      prvni_kladne = i
    posledni_kladne = i

# Součet prvků mezi prvním a posledním kladným prvkem
if prvni_kladne is not None and posledni_kladne is not None:
  for i in range(prvni_kladne + 1, posledni_kladne + 1):
    soucet_kladne += seznam[i]

# Výpis výsledků
print(f"Seznam náhodných čísel: {seznam}")
print(f"Součet záporných čísel: {soucet_zapornych}")
print(f"Součet sudých čísel: {soucet_suchych}")
print(f"Součet lichých čísel: {soucet_lichych}")
print(f"Součin prvků s indexy dělitelnými 3: {soucin_3_index}")
print(f"Součin prvků mezi nejmenším a největším prvkem: {soucin_min_max}")
print(f"Součet prvků mezi prvním a posledním kladným prvkem: {soucet_kladne}")