import json

def ulozit_seznam_do_souboru(seznam_cisel, nazev_souboru):
  """
  Uloží zadaný seznam čísel do souboru v JSON formátu.

  Argumenty:
    seznam_cisel: Seznam celých čísel, která se mají uložit.
    nazev_souboru: Název souboru, do kterého se data uloží.
  """
  # Převod seznamu na JSON
  json_data = json.dumps(seznam_cisel)

  # Otevření souboru v režimu zápisu
  with open(nazev_souboru, "w") as soubor:
    # Zapsání JSON dat do souboru
    soubor.write(json_data)

def nacist_seznam_ze_souboru(nazev_souboru):
  """
  Načte seznam čísel ze souboru v JSON formátu a vrátí ho.

  Argumenty:
    nazev_souboru: Název souboru, ze kterého se data načtou.

  Vrací:
    Seznam celých čísel načtených ze souboru.
  """
  # Otevření souboru v režimu čtení
  with open(nazev_souboru, "r") as soubor:
    # Načtení JSON dat ze souboru
    json_data = soubor.read()

  # Převedení JSON dat na seznam
  seznam_cisel = json.loads(json_data)

  # Vrácení seznamu
  return seznam_cisel

# Získat seznam čísel od uživatele
seznam_cisel = input("Zadejte seznam celých čísel, oddělených čárkami: ").split(",")
seznam_cisel = [int(x) for x in seznam_cisel]

# Uložit seznam do souboru
nazev_souboru = "seznam_cisel.json"
ulozit_seznam_do_souboru(seznam_cisel, nazev_souboru)
print(f"Seznam čísel byl uložen do souboru {nazev_souboru}.")

# Načíst seznam ze souboru
nacteny_seznam = nacist_seznam_ze_souboru(nazev_souboru)
print(f"Načtený seznam čísel: {nacteny_seznam}")
