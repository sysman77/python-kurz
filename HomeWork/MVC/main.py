from controller import *
from view import *
def run():
    controller = BotyController()
    view = BotyView()

    while True:
        print("\nMožnosti:")
        print("1. Přidat boty")
        print("2. Zobrazit všechny boty")
        print("3. Přidat boty do košíku")
        print("4. Zobrazit košík")
        print("5. Odstranit boty z košíku")
        print("6. Zaplatit")
        print("7. Konec")

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
            index = int(input("Zadejte index boty k přidání do košíku (počínaje 0): "))
            if 0 <= index < len(controller.boty_list):
                boty = controller.boty_list[index]
                controller.pridat_do_kosiku(boty)
                view.zobrazit_zpravu(f'Boty {boty.znacka} přidány do košíku.')
            else:
                view.zobrazit_zpravu('Neplatný index.')

        elif volba == '4':
            kosik = controller.zobrazit_kosik()
            view.zobrazit_kosik(kosik)

        elif volba == '5':
            index = int(input("Zadejte index boty k odstranění z košíku (počínaje 0): "))
            kosik = controller.zobrazit_kosik()
            if 0 <= index < len(kosik):
                boty = kosik[index]
                controller.odstranit_z_kosiku(boty)
                view.zobrazit_zpravu(f'Boty {boty.znacka} odstraněny z košíku.')
            else:
                view.zobrazit_zpravu('Neplatný index.')

        elif volba == '6':
            metoda = input("Zadejte metodu platby (hotově/kartou): ")
            zprava = controller.zaplatit(metoda)
            view.zobrazit_zpravu(zprava)

        elif volba == '7':
            print("Konec programu.")
            break

        else:
            view.zobrazit_zpravu("Neplatná volba, zkuste to znovu.")


# Spuštění programu
if __name__ == "__main__":
    run()
