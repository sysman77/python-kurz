opakovani = "y"
while opakovani == "y":
    # zadani mesice
  mesic = input("Zadej název nebo číslo měsíce: ")

  obdobi = None
  # vyhodnocení ročního období
  if mesic in ["prosinec", "leden", "únor", "12", "1", "2"]:
     obdobi = "zima"
  elif mesic in ["březen", "duben", "květen", "3", "4", "5"]:
    obdobi = "jaro"
  elif mesic in ["červen", "červenec", "srpen", "6", "7", "8"]:
        obdobi = "léto"
  elif mesic in ["září", "říjen", "listopad", "9", "10", "11"]:
        obdobi = "podzim"
  else:
        obdobi = "Asi překlep nebo zadán nesmysl"

    # vypis vysledku
  print(f"Roční období pro měsíc {mesic} je {obdobi}.")

  opakovani = input("Chceš pokračovat? -> y: ")
  if opakovani != "y":
     break


print("Konec")

