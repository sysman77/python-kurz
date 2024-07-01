"""
Multiple inheritance
Vytvořte dvě základní třídy ElektrickéZařízení a VoděOdolnéZařízení a poté vytvořit třetí třídu ChytrýHodinky,
která bude dědit vlastnosti od obou základních tříd, demonstrující koncept vícenásobné dědičnosti v Pythonu.
ElectricalDevice with methods turn_on() and turn_off()
WaterResistantDevice with method waterproof()
"""

class ElektrickéZařízení:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Zařízení je zapnuto.")
        else:
            print("Zařízení je již zapnuto.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Zařízení je vypnuto.")
        else:
            print("Zařízení je již vypnuto.")


class VoděOdolnéZařízení:
    def waterproof(self):
        print("Zařízení je voděodolné.")


class ChytréHodinky(ElektrickéZařízení, VoděOdolnéZařízení):
    def __init__(self):
        ElektrickéZařízení.__init__(self)  # Inicializace základní třídy ElektrickéZařízení


# Příklady použití:
hodinky = ChytréHodinky()

# Testování metod
hodinky.turn_on()  # Zařízení je zapnuto.
hodinky.turn_off()  # Zařízení je vypnuto.
hodinky.waterproof()  # Zařízení je voděodolné.
