def pocitej_vyskyt_ovoc(ntice_ovoc, hledane_ovoce):
  """
  Funkce pro počítání výskytu ovoce v n-tici, včetně výskytů v částech prvků.

  Argumenty:
    ntice_ovoc: N-tice názvů ovoce.
    hledane_ovoce: Název ovoce k nalezení.

  Vrací:
    Počet výskytů hledaného ovoce v n-tici (včetně dílčích výskytů).
  """

  pocet_vyskytu = 0

  for ovoce in ntice_ovoc:
    # Převedení na malá písmena
    ovoce_male = ovoce.lower()
    hledane_ovoce_male = hledane_ovoce.lower()

    # Kontrola celkového shodu
    if ovoce_male == hledane_ovoce_male:
      pocet_vyskytu += 1

    # Kontrola dílčích shod
    elif hledane_ovoce_male in ovoce_male:
      pocet_vyskytu += 1

  return pocet_vyskytu

# Příklad použití
ntice_ovoc = ("banán", "jablko", "banánmango", "mango", "jahoda-banán")
hledane_ovoce = input("Zadejte název ovoce: ")

pocet_vyskytu = pocitej_vyskyt_ovoc(ntice_ovoc, hledane_ovoce)

print(f"Ovoce '{hledane_ovoce}' se v n-tici vyskytuje {pocet_vyskytu}krát.")
