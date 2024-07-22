class BotyView:
    @staticmethod
    def zobrazit_boty(boty):
        print(boty)

    @staticmethod
    def zobrazit_vsechny_boty(boty_list):
        for boty in boty_list:
            print(boty)

    @staticmethod
    def zobrazit_kosik(kosik_list):
        if not kosik_list:
            print("Košík je prázdný.")
        for boty in kosik_list:
            print(boty)
        print(f'Celková cena: {sum(boty.cena for boty in kosik_list)} Kč')

    @staticmethod
    def zobrazit_zpravu(zprava):
        print(zprava)
