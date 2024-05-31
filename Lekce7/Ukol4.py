def main():
  
  knihy = {}  # Slovník pro ukládání informací o knihách

  while True:
    print("\nMožnosti:")
    print("1. Přidat knihu")
    print("2. Smazat knihu")
    print("3. Vyhledat knihu")
    print("4. Nahradit informace o knize")
    print("5. Ukončit")

    volba = input("Zadejte číslo volby: ")

    if volba == "1":
      nazev = input("Zadejte název knihy: ")
      autor = input("Zadejte jméno autora: ")
      zanr = input("Zadejte žánr knihy: ")
      rok = int(input("Zadejte rok vydání: "))
      vydavatel = input("Zadejte vydavatele: ")

      knihy[nazev] = {
          "autor": autor,
          "zanr": zanr,
          "rok": rok,
          "vydavatel": vydavatel
      }
      print(f"Kniha '{nazev}' byla přidána.")

    elif volba == "2":
      nazev = input("Zadejte název knihy, kterou chcete smazat: ")
      if nazev in knihy:
        del knihy[nazev]
        print(f"Kniha '{nazev}' byla smazána.")
      else:
        print(f"Kniha '{nazev}' nebyla nalezena.")

    elif volba == "3":
      hledany_text = input("Zadejte text pro vyhledávání (název, autor, žánr): ")
      nalezene_knihy = []
      for nazev, kniha in knihy.items():
        if hledany_text.lower() in nazev.lower() or \
           hledany_text.lower() in kniha["autor"].lower() or \
           hledany_text.lower() in kniha["zanr"].lower():
          nalezene_knihy.append(nazev)

      if nalezene_knihy:
        print(f"Nalezené knihy: {', '.join(nalezene_knihy)}")
      else:
        print(f"Byla nalezena.")

    elif volba == "4":
      nazev = input("Zadejte název knihy, jejíž informace chcete nahradit: ")
      if nazev in knihy:
        kniha = knihy[nazev]

        novy_autor = input(f"Zadejte nové jméno autora ({kniha['autor']}): ")
        novy_zanr = input(f"Zadejte nový žánr knihy ({kniha['zanr']}): ")
        novy_rok = int(input(f"Zadejte nový rok vydání ({kniha['rok']}): "))
        novy_vydavatel = input(f"Zadejte nového vydavatele ({kniha['vydavatel']}): ")

        knihy[nazev] = {
            "autor": novy_autor or kniha["autor"],
            "zanr": novy_zanr or kniha["zanr"],
            "rok": novy_rok or kniha["rok"],
            "vydavatel": novy_vydavatel or kniha["vydavatel"]
        }
        print(f"Informace o knize '{nazev}' byly aktualizovány.")
      else:
        print(f"Kniha '{nazev}' nebyla nalezena.")

    elif volba == "5":
        print("Ukončuji program.")
        break

    else:
        print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
  main()
