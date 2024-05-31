def main():
  
  slovnik = {}  # Slovník pro ukládání slov a překladů

  while True:
    print("\nMožnosti:")
    print("1. Přidat slovo")
    print("2. Smazat slovo")
    print("3. Vyhledat slovo")
    print("4. Nahradit překlad")
    print("5. Ukončit")

    volba = input("Zadejte číslo volby: ")

    if volba == "1":
      anglicke_slovo = input("Zadejte anglické slovo: ")
      cesky_preklad = input("Zadejte český překlad: ")
      slovnik[anglicke_slovo] = cesky_preklad
      print(f"Slovo '{anglicke_slovo}' s překladem '{cesky_preklad}' bylo přidáno.")

    elif volba == "2":
      anglicke_slovo = input("Zadejte anglické slovo, které chcete smazat: ")
      if anglicke_slovo in slovnik:
        del slovnik[anglicke_slovo]
        print(f"Slovo '{anglicke_slovo}' bylo smazáno.")
      else:
        print(f"Slovo '{anglicke_slovo}' nebylo nalezeno.")

    elif volba == "3":
      anglicke_slovo = input("Zadejte anglické slovo, které chcete vyhledat: ")
      if anglicke_slovo in slovnik:
        cesky_preklad = slovnik[anglicke_slovo]
        print(f"Anglické slovo '{anglicke_slovo}' se překládá jako '{cesky_preklad}'.")
      else:
        print(f"Slovo '{anglicke_slovo}' nebylo nalezeno.")

    elif volba == "4":
      anglicke_slovo = input("Zadejte anglické slovo, jehož překlad chcete nahradit: ")
      if anglicke_slovo in slovnik:
        novy_cesky_preklad = input("Zadejte nový český překlad: ")
        slovnik[anglicke_slovo] = novy_cesky_preklad
        print(f"Překlad slova '{anglicke_slovo}' byl aktualizován na '{novy_cesky_preklad}'.")
      else:
        print(f"Slovo '{anglicke_slovo}' nebylo nalezeno.")

    elif volba == "5":
      print("Ukončuji program.")
      break

    else:
      print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
  main()
