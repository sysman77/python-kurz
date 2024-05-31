def aktualizuj_ntici(ntice_znacek, index, nova_hodnota):
  """
  Funkce pro aktualizaci n-tice značek aut.

  Argumenty:
    ntice_znacek: Původní n-tice značek aut.
    index: Index prvku k aktualizaci.
    nova_hodnota: Nová hodnota pro daný index.

  Vrací:
    Novou n-tici s aktualizovanou hodnotou.
  """

  # Kontrola platnosti indexu
  if index < 0 or index >= len(ntice_znacek):
    print("Neplatný index.")
    return ntice_znacek

  # Vytvoření nového seznamu pro modifikaci
  novy_seznam = list(ntice_znacek)

  # Aktualizace prvku v seznamu
  novy_seznam[index] = nova_hodnota

  # Konverze seznamu zpět na n-tici
  return tuple(novy_seznam)

# Příklad použití
ntice_znacek = ("Škoda", "Volkswagen", "Audi", "BMW", "Mercedes")
print(ntice_znacek)
novy_index = int(input("Zadejte index prvku k aktualizaci: "))
nova_hodnota = input("Zadejte novou hodnotu: ")

aktualizovana_ntice = aktualizuj_ntici(ntice_znacek, novy_index, nova_hodnota)

print(aktualizovana_ntice)

