import random

# Vytvoření dvou seznamů s náhodnými čísly
seznam1 = [random.randint(1, 20) for _ in range(10)]
seznam2 = [random.randint(1, 20) for _ in range(10)]

# Vytvoření prázdného seznamu pro třetí seznam
seznam3 = []

# Procházení prvků v prvním seznamu
for prvek in seznam1:
  # Kontrola, zda prvek existuje v druhém seznamu
  if prvek in seznam2:
    seznam3.append(prvek)

print(f"Seznam 1: {seznam1}")
print(f"Seznam 2: {seznam2}")
print(f"Seznam 3: {seznam3}")
