class BotyView:
    @staticmethod
    def zobrazit_boty(boty):
        print(boty)

    @staticmethod
    def zobrazit_vsechny_boty(boty_list):
        for boty in boty_list:
            print(boty)

    @staticmethod
    def zobrazit_boty_podle_znacky(boty_list, znacka):
        print(f'Boty od značky {znacka}:')
        for boty in boty_list:
            print(boty)
