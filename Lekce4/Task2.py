from random import randint

# Vytvoření seznamu náhodných čísel
seznam = [randint(-10, 10) for _ in range(10)]

# Inicializace prázdných seznamů pro sudá, lichá, záporná a kladná čísla
sudá = []
lichá = []
záporná = []
kladná = []

# Procházení seznamu a zařazování čísel do odpovídajících seznamů
for cislo in seznam:
  if cislo % 2 == 0:
    sudá.append(cislo)
  else:
    lichá.append(cislo)
  if cislo < 0:
    záporná.append(cislo)
  else:
    kladná.append(cislo)

# Výpis výsledků
print(f"Původní seznam: {seznam}")
print(f"Seznam sudých čísel: {sudá}")
print(f"Seznam lichých čísel: {lichá}")
print(f"Seznam záporných čísel: {záporná}")
print(f"Seznam kladných čísel: {kladná}")