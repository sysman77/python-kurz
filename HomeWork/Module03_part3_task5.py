import random

# Vytvoření dvou seznamů s náhodnými čísly
seznam1 = [random.randint(1, 20) for _ in range(10)]
seznam2 = [random.randint(1, 20) for _ in range(10)]

# Vytvoření prázdného seznamu pro třetí seznam
seznam3 = []

# Procházení prvků v Seznamu 1
for i, prvek1 in enumerate(seznam1):
  # Vytvoření dvojice s nejmenší a největší hodnotou
  min_max = (min(prvek1, seznam2[i]), max(prvek1, seznam2[i]))

  # Kontrola, zda je dvojice v Seznamu 3
  if min_max not in seznam3:
    seznam3.append(min_max)

print(f"Seznam 1: {seznam1}")
print(f"Seznam 2: {seznam2}")
print(f"Seznam 3: {seznam3}")
