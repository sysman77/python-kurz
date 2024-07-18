from controller import *
from view import *


def run():
    controller = BotyController()
    view = BotyView()

    while True:
        print("\nMožnosti:")
        print("1. Přidat boty")
        print("2. Zobrazit všechny boty")
        print("3. Najít boty podle značky")
        print("4. Konec")

        volba = input("Zadejte číslo možnosti: ")

        if volba == '1':
            druh = input("Zadejte druh bot (mužský/ženský): ")
            typ = input("Zadejte typ obuvi (tenisky, boty, sandály, společenské boty atd.): ")
            barva = input("Zadejte barvu: ")
            cena = float(input("Zadejte cenu: "))
            znacka = input("Zadejte značku: ")
            velikost = int(input("Zadejte velikost: "))
            boty = controller.pridat_boty(druh, typ, barva, cena, znacka, velikost)
            view.zobrazit_boty(boty)

        elif volba == '2':
            vsechny_boty = controller.zobrazit_vsechny_boty()
            view.zobrazit_vsechny_boty(vsechny_boty)

        elif volba == '3':
            znacka = input("Zadejte značku: ")
            boty_znacky = controller.najit_boty_podle_znacky(znacka)
            view.zobrazit_boty_podle_znacky(boty_znacky, znacka)

        elif volba == '4':
            print("Konec programu.")
            break

        else:
            print("Neplatná volba, zkuste to znovu.")


# Spuštění programu
if __name__ == "__main__":
    run()
