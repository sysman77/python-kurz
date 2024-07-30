from model import *
from view import *


class PizzeriaController:
    def __init__(self):
        self.prodeje = Prodeje()
        self.aktualni_objednavka = None

    def spustit(self):
        while True:
            UI.zobrazit_menu()
            volba = UI.ziskat_vstup("Vyberte možnost: ")
            if volba == '1':
                self.vytvorit_objednavku()
            elif volba == '2':
                self.zaplatit_objednavku()
            elif volba == '3':
                self.admin_menu()
            elif volba == '4':
                break
            else:
                print("Neplatná volba, zkuste to znovu.")

    def vytvorit_objednavku(self):
        UI.zobrazit_pizza_menu()
        volba = UI.ziskat_vstup("Vyberte možnost: ")
        if volba == 'a':
            self.vytvorit_standardni_pizzu()
        elif volba == 'b':
            self.vytvorit_vlastni_pizzu()
        else:
            print("Neplatná volba, zkuste to znovu.")

    def vytvorit_standardni_pizzu(self):
        self.aktualni_objednavka = Objednavka()
        pizza = Pizza("Standardní", 200)
        UI.zobrazit_pridavky_menu()
        pridavek_volba = UI.ziskat_vstup("Chcete přidat přílohy? (ano/ne): ")
        if pridavek_volba.lower() == 'ano':
            self.pridat_pridavky(pizza)
        self.aktualni_objednavka.pridat_pizzu(pizza)
        SpravceSouboru.ulozit_objednavku(self.aktualni_objednavka)
        print("Objednávka vytvořena úspěšně.")

    def vytvorit_vlastni_pizzu(self):
        self.aktualni_objednavka = Objednavka()
        nazev_pizzy = UI.ziskat_vstup("Zadejte název pizzy: ")
        pizza = Pizza(nazev_pizzy, 250)
        self.pridat_pridavky(pizza)
        self.aktualni_objednavka.pridat_pizzu(pizza)
        SpravceSouboru.ulozit_objednavku(self.aktualni_objednavka)
        print("Objednávka vytvořena úspěšně.")

    def pridat_pridavky(self, pizza):
        pridavky = {
            'Sladká cibule': Pridavek('Sladká cibule', 20),
            'Jalapenos': Pridavek('Jalapenos', 20),
            'Chile': Pridavek('Chile', 20),
            'Okurky': Pridavek('Okurky', 20),
            'Prosciutto': Pridavek('Prosciutto', 50)
        }
        while True:
            UI.zobrazit_pridavky_menu()
            pridavek_volba = UI.ziskat_vstup("Zadejte název přílohy (nebo 'hotovo' pro ukončení): ")
            if pridavek_volba.lower() == 'hotovo':
                break
            if pridavek_volba in pridavky:
                pizza.pridat_pridavek(pridavky[pridavek_volba])
            else:
                print("Neplatná příloha, zkuste to znovu.")

    def zaplatit_objednavku(self):
        if not self.aktualni_objednavka:
            print("Není žádná objednávka k zaplacení.")
            return
        print("Detaily aktuální objednávky:")
        print(self.aktualni_objednavka)
        metoda = UI.ziskat_vstup("Vyberte způsob platby (hotovost/karta): ")
        try:
            platba_metoda = Parser.parse_platba_metoda(metoda)
            platba_metoda.zaplatit(self.aktualni_objednavka.spocitat_celkem())
            self.prodeje.zaznamenat_objednavku(self.aktualni_objednavka)
            self.aktualni_objednavka = None
            print("Platba byla úspěšná.")
        except ValueError as e:
            print(e)

    def admin_menu(self):
        heslo = UI.ziskat_vstup("Zadejte admin heslo: ")
        if heslo == "admin123":
            print(self.prodeje.ziskat_souhrn_prodeju())
        else:
            print("Neoprávněný přístup.")
