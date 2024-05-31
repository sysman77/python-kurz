# Napište rekurzivní funkci, která vezme seznam 100 náhodných celých čísel a najde pozici, na které začíná posloupnost 10 čísel, a jejich součet musí být nejmenší.

import random

def najdi_nejmensi_soucet_10(seznam, pozice, aktualni_soucet, minimalni_soucet, minimalni_pozice):
 
  if pozice + 10 > len(seznam):
    return minimalni_pozice, minimalni_soucet

  novy_soucet = aktualni_soucet + seznam[pozice]

  if pozice == 0 or novy_soucet < minimalni_soucet:
    minimalni_pozice = pozice
    minimalni_soucet = novy_soucet

  return najdi_nejmensi_soucet_10(seznam, pozice + 1, novy_soucet, minimalni_soucet, minimalni_pozice)

def main():
  # Vytvoření seznamu 100 náhodných celých čísel
  seznam = [random.randint(-100, 100) for _ in range(100)]

  # Spuštění rekurzivní funkce
  pozice, soucet = najdi_nejmensi_soucet_10(seznam, 0, 0, float('inf'), -1)

  # Výpis výsledku
  print(f"Pozice s nejmenším součtem 10 čísel: {pozice}")
  print(f"Nejmenší součet 10 čísel: {soucet}")

if __name__ == "__main__":
  main()
