def soucin_v_rozsahu(pocatek, konec):

  # Ujistěte se, že počáteční číslo je vždy menší nebo rovno koncovému
  if pocatek > konec:
    pocatek, konec = konec, pocatek

  # Výpočet součinu
  soucin = 1
  for cislo in range(pocatek, konec + 1):
    soucin *= cislo

  # Vrácení součinu
  return soucin


soucin_revert = soucin_v_rozsahu(5, 2)
print(f"Součin čísel v rozsahu 5 až 2: {soucin_revert}")  # Vytiskne 120

soucin= soucin_v_rozsahu(2, 5)
print(f"Součin čísel v rozsahu 5 až 2: {soucin}")  # Vytiskne 120
