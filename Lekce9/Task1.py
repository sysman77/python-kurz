class Clovek:
  """Třída reprezentující osobu."""

  def __init__(self, cele_jmeno, datum_narozeni, kontaktni_cislo, mesto, zeme, adresa_bydliste):
    """Konstruktor třídy Člověk.

    Argumenty:
      cele_jmeno: Řetězec s celým jménem osoby.
      datum_narozeni: Objekt typu datetime.date s datem narození osoby.
      kontaktni_cislo: Řetězec s kontaktním číslem osoby.
      mesto: Řetězec s městem bydliště osoby.
      zeme: Řetězec se zemí bydliště osoby.
      adresa_bydliste: Řetězec s adresou bydliště osoby.
    """
    self.cele_jmeno = cele_jmeno
    self.datum_narozeni = datum_narozeni
    self.kontaktni_cislo = kontaktni_cislo
    self.mesto = mesto
    self.zeme = zeme
    self.adresa_bydliste = adresa_bydliste

  def __str__(self):
    """Metoda pro tisk informací o osobě.

    Vrací:
      Řetězec s informacemi o osobě.
    """
    return f"Jméno: {self.cele_jmeno}\nDatum narození: {self.datum_narozeni}\nKontaktní číslo: {self.kontaktni_cislo}\nMěsto: {self.mesto}\nZemě: {self.zeme}\nAdresa: {self.adresa_bydliste}"

  def vloz_cele_jmeno(self, cele_jmeno):
    """Metoda pro vložení celého jména osoby.

    Argumenty:
      cele_jmeno: Řetězec s celým jménem osoby.
    """
    self.cele_jmeno = cele_jmeno

  def ziskej_cele_jmeno(self):
    """Metoda pro získání celého jména osoby.

    Vrací:
      Řetězec s celým jménem osoby.
    """
    return self.cele_jmeno

  def vloz_datum_narozeni(self, datum_narozeni):
    """Metoda pro vložení data narození osoby.

    Argumenty:
      datum_narozeni: Objekt typu datetime.date s datem narození osoby.
    """
    self.datum_narozeni = datum_narozeni

  def ziskej_datum_narozeni(self):
    """Metoda pro získání data narození osoby.

    Vrací:
      Objekt typu datetime.date s datem narození osoby.
    """
    return self.datum_narozeni

  def vloz_kontaktni_cislo(self, kontaktni_cislo):
    """Metoda pro vložení kontaktního čísla osoby.

    Argumenty:
      kontaktni_cislo: Řetězec s kontaktním číslem osoby.
    """
    self.kontaktni_cislo = kontaktni_cislo

  def ziskej_kontaktni_cislo(self):
    """Metoda pro získání kontaktního čísla osoby.

    Vrací:
      Řetězec s kontaktním číslem osoby.
    """
    return self.kontaktni_cislo

  def vloz_mesto(self, mesto):
    """Metoda pro vložení města bydliště osoby.

    Argumenty:
      mesto: Řetězec s městem bydliště osoby.
    """
    self.mesto = mesto

  def ziskej_mesto(self):
    """Metoda pro získání města bydliště osoby.

    Vrací:
      Řetězec s městem bydliště osoby.
    """
    return self.mesto

  def vloz_zemi(self, zeme):
    """Metoda pro vložení země bydliště osoby.

    Argumenty:
      zeme: Řetězec se zemí bydliště osoby.
    """
    self.zeme = zeme

  def ziskej_zemi(self):
    """Metoda pro získání země bydliště osoby.

    Vrací:
      Řetězec se zemí bydliště osoby.
    """
    return self.zeme
