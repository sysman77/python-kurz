class Zeme:
  """Třída reprezentující zemi."""

  def __init__(self, nazev_zeme, kontinent, populace, volac_kod, hlavni_mesto, nazvy_mest):
    """Konstruktor třídy Země.

    Argumenty:
      nazev_zeme: Řetězec s názvem země.
      kontinent: Řetězec s názvem kontinentu.
      populace: Celé číslo s populací země.
      volac_kod: Řetězec s telefonním kódem země.
      hlavni_mesto: Řetězec s názvem hlavního města.
      nazvy_mest: Seznam řetězců s názvy dalších měst v zemi.
    """
    self.nazev_zeme = nazev_zeme
    self.kontinent = kontinent
    self.populace = populace
    self.volac_kod = volac_kod
    self.hlavni_mesto = hlavni_mesto
    self.nazvy_mest = nazvy_mest

  def __str__(self):
    """Metoda pro tisk informací o zemi.

    Vrací:
      Řetězec s informacemi o zemi.
    """
    return f"Název země: {self.nazev_zeme}\nKontinent: {self.kontinent}\nPopulace: {self.populace}\nTelefonní kód: {self.volac_kod}\nHlavní město: {self.hlavni_mesto}\nMěsta: {', '.join(self.nazvy_mest)}"

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

  def vloz_kontinent(self, kontinent):
    """Metoda pro vložení kontinentu.

    Argumenty:
      kontinent: Řetězec s názvem kontinentu.
    """
    self.kontinent = kontinent

  def ziskej_kontinent(self):
    """Metoda pro získání kontinentu.

    Vrací:
      Řetězec s názvem kontinentu.
    """
    return self.kontinent

  def vloz_populace(self, populace):
    """Metoda pro vložení populace.

    Argumenty:
      populace: Celé číslo s populací země.
    """
    self.populace = populace

  def ziskej_populace(self):
    """Metoda pro získání populace.

    Vrací:
      Celé číslo s populací země.
    """
    return self.populace

  def vloz_volac_kod(self, volac_kod):
    """Metoda pro vložení telefonního kódu.

    Argumenty:
      volac_kod: Řetězec s telefonním kódem země.
    """
    self.volac_kod = volac_kod

  def ziskej_volac_kod(self):
    """Metoda pro získání telefonního kódu.

    Vrací:
      Řetězec s telefonním kódem země.
    """
    return self.volac_kod

  def vloz_hlavni_mesto(self, hlavni_mesto):
    """Metoda pro vložení názvu hlavního města.

    Argumenty:
      hlavni_mesto: Řetězec s názvem hlavního města.
    """
    self.hlavni_mesto = hlavni_mesto

  def ziskej_hlavni_mesto(self):
    """Metoda pro získání názvu hlavního města.

    Vrací:
      Řetězec s názvem hlavního města.
    """
    return self.hlavni_mesto

  def vloz_nazvy_mest(self, nazvy_mest):
    """Metoda pro vložení seznamu názvů měst"""

