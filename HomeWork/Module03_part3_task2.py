import random

# Vytvoření dvou seznamů s náhodnými čísly
seznam1 = [random.randint(1, 20) for _ in range(10)]
seznam2 = [random.randint(1, 20) for _ in range(10)]

# Vytvoření sady obsahující jedinečné prvky ze dvou seznamů
sada = set(seznam1 + seznam2)

# Převedení sady na seznam
seznam3 = list(sada)

print(f"Seznam 1: {seznam1}")
print(f"Seznam 2: {seznam2}")
print(f"Seznam 3: {seznam3}")
