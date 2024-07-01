"""
Multiple inheritance
Vytvořte dvě základní třídy ElektrickéZařízení a VoděOdolnéZařízení a poté vytvořit třetí třídu ChytrýHodinky,
která bude dědit vlastnosti od obou základních tříd, demonstrující koncept vícenásobné dědičnosti v Pythonu.
ElectricalDevice with methods turn_on() and turn_off()
WaterResistantDevice with method waterproof()
"""

class ElektrickéZařízení:
  """
  Základní třída pro elektrická zařízení.
  """

  def __init__(self):
    self.is_turned_on = False

  def zapnout(self):
    """
    Zapne zařízení.
    """
    self.is_turned_on = True
    print(f"{self.__class__.__name__} se zapíná.")

  def vypnout(self):
    """
    Vypne zařízení.
    """
    self.is_turned_on = False
    print(f"{self.__class__.__name__} se vypíná.")


class VoděOdolnéZařízení:
  """
  Základní třída pro voděodolná zařízení.
  """

  def voděodolnost(self):
    """
    Simuluje akci voděodolnosti.
    """
    print(f"{self.__class__.__name__} je zařízení voděodolné.")


class ChytréHodinky(ElektrickéZařízení, VoděOdolnéZařízení):
  """
  Třída pro chytré hodinky, dědící z ElektrickéZařízení a VoděOdolnéZařízení.
  """

  def __init__(self):
    super().__init__()

  def zobrazit_notifikaci(self, notifikace):
    """
    Zobrazí notifikaci na chytrých hodinkách.
    """
    print(f"Notifikace: {notifikace}")


# Příklad použití

hodinky = ChytréHodinky()

hodinky.zapnout()
hodinky.zobrazit_notifikaci("Přijatý hovor")
hodinky.voděodolnost()
hodinky.vypnout()


"""
V tomto kódu:

Třída ElektrickéZařízení definuje metody zapnout() a vypnout(), které řídí zapnutí a vypnutí zařízení.
Třída VoděOdolnéZařízení definuje metodu voděodolnost(), která simuluje akci voděodolnosti.
Třída ChytréHodinky dědí z obou základních tříd, čímž získává jejich funkčnost. Může tak zapínat/vypínat a je 
voděodolná. Navíc má i vlastní metodu zobrazit_notifikaci() pro zobrazování notifikací.
Na konci kódu je uveden příklad použití, který demonstruje funkce chytrých hodinek.
Tento příklad ukazuje koncept vícenásobné dědičnosti v Pythonu. Třída ChytréHodinky kombinuje vlastnosti a funkčnost
 zděděné z obou základních tříd, čímž se stává komplexnějším a užitečnějším zařízením.
"""
