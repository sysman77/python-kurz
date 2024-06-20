class Mesto:
  """Třída reprezentující město."""

  def __init__(self, nazev_mesta, nazev_regionu, nazev_zeme, pocet_obcanu, psc, predcisli):
    """Konstruktor třídy Město.

    Argumenty:
      nazev_mesta: Řetězec s názvem města.
      nazev_regionu: Řetězec s názvem regionu, ve kterém se město nachází.
      nazev_zeme: Řetězec s názvem země, ve které se město nachází.
      pocet_obcanu: Celé číslo s počtem obyvatel města.
      psc: Řetězec s PSČ města.
      predcisli: Řetězec s předčíslím telefonních čísel ve městě.
    """
    self.nazev_mesta = nazev_mesta
    self.nazev_regionu = nazev_regionu
    self.nazev_zeme = nazev_zeme
    self.pocet_obcanu = pocet_obcanu
    self.psc = psc
    self.predcisli = predcisli

  def __str__(self):
    """Metoda pro tisk informací o městě.

    Vrací:
      Řetězec s informacemi o městě.
    """
    return f"Název města: {self.nazev_mesta}\nNázev regionu: {self.nazev_regionu}\nNázev země: {self.nazev_zeme}\nPočet obyvatel: {self.pocet_obcanu}\nPSČ: {self.psc}\nTelefonní předčíslí: {self.predcisli}"

  def vloz_nazev_mesta(self, nazev_mesta):
    """Metoda pro vložení názvu města.

    Argumenty:
      nazev_mesta: Řetězec s názvem města.
    """
    self.nazev_mesta = nazev_mesta

  def ziskej_nazev_mesta(self):
    """Metoda pro získání názvu města.

    Vrací:
      Řetězec s názvem města.
    """
    return self.nazev_mesta

  def vloz_nazev_regionu(self, nazev_regionu):
    """Metoda pro vložení názvu regionu.

    Argumenty:
      nazev_regionu: Řetězec s názvem regionu.
    """
    self.nazev_regionu = nazev_regionu

  def ziskej_nazev_regionu(self):
    """Metoda pro získání názvu regionu.

    Vrací:
      Řetězec s názvem regionu.
    """
    return self.nazev_regionu

  def vloz_nazev_zeme(self, nazev_zeme):
    """Metoda pro vložení názvu země.

    Argumenty:
      nazev_zeme: Řetězec s názvem země.
    """
    self.nazev_zeme = nazev_zeme

  def ziskej_nazev_zeme(self):
    """Metoda pro získání názvu země.

    Vrací:
      Řetězec s názvem země.
    """
    return self.nazev_zeme

  def vloz_pocet_obcanu(self, pocet_obcanu):
    """Metoda pro vložení počtu obyvatel.

    Argumenty:
      pocet_obcanu: Celé číslo s počtem obyvatel.
    """
    self.pocet_obcanu = pocet_obcanu

  def ziskej_pocet_obcanu(self):
    """Metoda pro získání počtu obyvatel.

    Vrací:
      Celé číslo s počtem obyvatel.
    """
    return self.pocet_obcanu

  def vloz_psc(self, psc):
    """Metoda pro vložení PSČ.

    Argumenty:
      psc: Řetězec s PSČ.
    """
    self.psc = psc

  def ziskej_psc(self):
    """Metoda pro získání PSČ.

    Vrací:
      Řetězec s PSČ.
    """
    return self.psc

