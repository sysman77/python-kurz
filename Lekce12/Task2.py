import json

def nacist_data(soubor="data.json"):
  """Načte data ze souboru v JSON formátu a vrátí seznam čísel."""
  try:
    with open(soubor, "r") as soubor:
      data = json.load(soubor)
    return data
  except (FileNotFoundError, json.JSONDecodeError):
    print(f"Soubor '{soubor}' neexistuje nebo obsahuje neplatná data. Vytvořen nový prázdný seznam.")
    return []

def ulozit_data(data, soubor="data.json"):
  """Uloží seznam čísel do souboru v JSON formátu."""
  with open(soubor, "w") as soubor:
    json.dump(data, soubor)

def zobrazit_seznam(data):
  """Vytiskne seznam čísel na konzoli."""
  if not data:
    print("Seznam je prázdný.")
  else:
    print(data)

def pridat_data(data):
  """Přidá do seznamu zadané číslo."""
  cislo = int(input("Zadejte číslo, které chcete přidat: "))
  data.append(cislo)
  print(f"Číslo {cislo} bylo přidáno do seznamu.")

def smazat_data(data):
  """Smaže ze seznamu zadané číslo."""
  if not data:
    print("Seznam je prázdný. Není co mazat.")
    return

  cislo = int(input("Zadejte číslo, které chcete smazat: "))
  if cislo in data:
    data.remove(cislo)
    print(f"Číslo {cislo} bylo smazáno ze seznamu.")
  else:
    print(f"Číslo {cislo} v seznamu neexistuje.")

def main():
  """Hlavní funkce programu."""
  data = nacist_data()

  while True:
    print("\nMenu:")
    print("1. Načíst data")
    print("2. Uložit data")
    print("3. Přidat data")
    print("4. Smazat data")
    print("5. Zobrazit seznam")
    print("0. Ukončit")

    volba = input("Zadejte číslo volby: ")

    if volba == "0":
      break
    elif volba == "1":
      data = nacist_data()
      print("Data byla načtena ze souboru.")
    elif volba == "2":
      ulozit_data(data)
      print("Data byla uložena do souboru.")
    elif volba == "3":
      pridat_data(data)
    elif volba == "4":
      smazat_data(data)
    elif volba == "5":
      zobrazit_seznam(data)
    else:
      print("Neplatná volba.")

  # Uložení dat před ukončením
  ulozit_data(data)

if __name__ == "__main__":
  main()
