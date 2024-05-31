def pocitej_vyskyt_ovoc(ntice_ovoc, hledane_ovoce):
  """
  Funkce pro počítání výskytu ovoce v n-tici.

  Argumenty:
    ntice_ovoc: N-tice názvů ovoce.
    hledane_ovoce: Název ovoce k nalezení.

  Vrací:
    Počet výskytů hledaného ovoce v n-tici.
  """

  pocet_vyskytu = 0

  # Procházení prvků n-tice
  for ovoce in ntice_ovoc:
    # Porovnání s hledaným ovocem (s převodem na malá písmena)
    if ovoce.lower() == hledane_ovoce.lower():
      pocet_vyskytu += 1

  return pocet_vyskytu

# Příklad použití
ntice_ovoc = ("jablko", "hruška", "banán", "jablko", "mango", "hruška")
hledane_ovoce = input("Zadejte název ovoce: ")

pocet_vyskytu = pocitej_vyskyt_ovoc(ntice_ovoc, hledane_ovoce)

print(f"Ovoce '{hledane_ovoce}' se v n-tici vyskytuje {pocet_vyskytu}krát.")
