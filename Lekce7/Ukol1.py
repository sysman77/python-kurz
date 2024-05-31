def main():
  
  hraci = {}  # Slovník pro ukládání informací o hráčích

  while True:
    print("\nMožnosti:")
    print("1. Přidat hráče")
    print("2. Smazat hráče")
    print("3. Vyhledat hráče")
    print("4. Nahradit informace o hráči")
    print("5. Ukončit")

    volba = input("Zadejte číslo volby: ")

    if volba == "1":
      jmeno = input("Zadejte jméno hráče: ")
      vyska = float(input("Zadejte výšku hráče (v cm): "))
      hraci[jmeno] = vyska
      print(f"Hráč {jmeno} s výškou {vyska} cm byl přidán.")

    elif volba == "2":
      jmeno = input("Zadejte jméno hráče, kterého chcete smazat: ")
      if jmeno in hraci:
        del hraci[jmeno]
        print(f"Hráč {jmeno} byl smazán.")
      else:
        print(f"Hráč {jmeno} nebyl nalezen.")

    elif volba == "3":
      jmeno = input("Zadejte jméno hráče, kterého chcete vyhledat: ")
      if jmeno in hraci:
        vyška = hraci[jmeno]
        print(f"Hráč {jmeno} má výšku {vyska} cm.")
      else:
        print(f"Hráč {jmeno} nebyl nalezen.")

    elif volba == "4":
      jmeno = input("Zadejte jméno hráče, jehož informace chcete nahradit: ")
      if jmeno in hraci:
        nova_vyska = float(input("Zadejte novou výšku hráče (v cm): "))
        hraci[jmeno] = nova_vyska
        print(f"Informace o hráči {jmeno} byly aktualizovány.")
      else:
        print(f"Hráč {jmeno} nebyl nalezen.")

    elif volba == "5":
      print("Ukončuji program.")
      break

    else:
      print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
  main()
