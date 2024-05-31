import random

# Vytvoření dvou seznamů s náhodnými čísly
seznam1 = [random.randint(1, 20) for _ in range(10)]
seznam2 = [random.randint(1, 20) for _ in range(10)]

# Vytvoření sady obsahující jedinečné prvky ze dvou seznamů

seznam3 = []
for item in seznam1:
    if item not in seznam3:
        seznam3.append(item)

for item in seznam2:
    if item not in seznam3:
        seznam3.append(item)

print(f"Seznam 1: {seznam1}")
print(f"Seznam 2: {seznam2}")
print(f"Seznam 3: {seznam3}")