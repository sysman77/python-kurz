import random

# Vytvoření dvou seznamů s náhodnými čísly
seznam1 = [random.randint(1, 20) for _ in range(10)]
seznam2 = [random.randint(1, 20) for _ in range(10)]

# Vytvoření prázdných seznamů pro jedinečné prvky
seznam_jedinečné1 = []
seznam_jedinečné2 = []

# Procházení prvků v Seznamu 1
for prvek in seznam1:
  # Kontrola, zda prvek není v Seznamu 2
  if prvek not in seznam2:
    seznam_jedinečné1.append(prvek)

# Procházení prvků v Seznamu 2
for prvek in seznam2:
  # Kontrola, zda prvek není v Seznamu 1
  if prvek not in seznam1:
    seznam_jedinečné2.append(prvek)

print(f"Seznam 1: {seznam1}")
print(f"Seznam 2: {seznam2}")
print(f"Jedinečné prvky v Seznamu 1: {seznam_jedinečné1}")
print(f"Jedinečné prvky v Seznamu 2: {seznam_jedinečné2}")
