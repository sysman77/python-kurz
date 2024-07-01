"""
Přidejte do třídy Human statickou metodu, která po zavolání vrátí počet vytvořených objektů třídy Human.
"""
class Human:
    # Atribut třídy pro sledování počtu vytvořených objektů
    _count = 0

    def __init__(self, name):
        self.name = name
        # Při každém vytvoření instance třídy Human se zvýší počet o 1
        Human._count += 1

    @staticmethod
    def get_count():
        # Statická metoda pro vrácení počtu vytvořených objektů
        return Human._count

# Příklady použití:
h1 = Human("Alice")
h2 = Human("Bob")
h3 = Human("Charlie")

# Volání statické metody pro získání počtu vytvořených objektů
print(f"Počet vytvořených objektů třídy Human: {Human.get_count()}")  # Počet vytvořených objektů třídy Human: 3
