class IntegerStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if self.is_full():
            print("Zásobník je plný. Nelze vložit nové číslo.")
        else:
            self.stack.append(value)
            print(f"Číslo {value} bylo vloženo do zásobníku.")

    def pop(self):
        if self.is_empty():
            print("Zásobník je prázdný. Nelze vytlačit číslo.")
        else:
            value = self.stack.pop()
            print(f"Číslo {value} bylo vytlačeno ze zásobníku.")
            return value

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []
        print("Zásobník byl vyčištěn.")

    def top(self):
        if self.is_empty():
            print("Zásobník je prázdný. Není žádné číslo na vrcholu.")
        else:
            return self.stack[-1]


def menu():
    print("\nNabídka operací se zásobníkem:")
    print("1. Vložení celého čísla do zásobníku")
    print("2. Vytlačení celého čísla ze zásobníku")
    print("3. Počítání počtu celých čísel v zásobníku")
    print("4. Kontrola, zda je zásobník prázdný")
    print("5. Kontrola, zda je zásobník plný")
    print("6. Vyčištění zásobníku")
    print("7. Získání hodnoty horního celého čísla ze zásobníku")
    print("8. Konec")


def main():
    size = int(input("Zadejte velikost zásobníku: "))
    stack = IntegerStack(size)




if __name__ == "__main__":
    main()
