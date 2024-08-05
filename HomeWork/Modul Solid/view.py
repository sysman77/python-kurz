class UI:
    @staticmethod
    def zobrazit_menu():
        print("1. Vytvoření objednávky")
        print("2. Zaplatit")
        print("3. Admin menu")
        print("4. Konec")

    @staticmethod
    def zobrazit_pizza_menu():
        print("a. Standardní pizza")
        print("b. Vlastní pizza")

    @staticmethod
    def zobrazit_pridavky_menu():
        print("Dostupné přílohy: Cibule, Jalapenos, Chilli, Houby, Prosciutto")

    @staticmethod
    def ziskat_vstup(prompt):
        return input(prompt)