def main():
  
  zamestnanci = {}  # Slovník pro ukládání informací o zaměstnancích

  while True:
    print("\nMožnosti:")
    print("1. Přidat zaměstnance")
    print("2. Smazat zaměstnance")
    print("3. Vyhledat zaměstnance")
    print("4. Nahradit informace o zaměstnanci")
    print("5. Ukončit")

    volba = input("Zadejte číslo volby: ")

    if volba == "1":
      jmeno = input("Zadejte celé jméno: ")
      telefon = input("Zadejte telefonní číslo: ")
      email = input("Zadejte firemní e-mail: ")
      pozice = input("Zadejte pracovní zařazení: ")
      pokoj = input("Zadejte číslo pokoje: ")
      skype = input("Zadejte Skype jméno: ")

      zamestnanci[jmeno] = {
          "telefon": telefon,
          "email": email,
          "pozice": pozice,
          "pokoj": pokoj,
          "skype": skype
      }
      print(f"Zaměstnanec {jmeno} byl přidán.")

    elif volba == "2":
      jmeno = input("Zadejte jméno zaměstnance, kterého chcete smazat: ")
      if jmeno in zamestnanci:
        del zamestnanci[jmeno]
        print(f"Zaměstnanec {jmeno} byl smazán.")
      else:
        print(f"Zaměstnanec {jmeno} nebyl nalezen.")

    elif volba == "3":
      jmeno = input("Zadejte jméno zaměstnance, kterého chcete vyhledat: ")
      if jmeno in zamestnanci:
        zamestnanec = zamestnanci[jmeno]
        print(f"""
Jméno: {jmeno}
Telefon: {zamestnanec["telefon"]}
E-mail: {zamestnanec["email"]}
Pozice: {zamestnanec["pozice"]}
Číslo pokoje: {zamestnanec["pokoj"]}
Skype: {zamestnanec["skype"]}
""")
      else:
        print(f"Zaměstnanec {jmeno} nebyl nalezen.")

    elif volba == "4":
      jmeno = input("Zadejte jméno zaměstnance, jehož informace chcete nahradit: ")
      if jmeno in zamestnanci:
        zamestnanec = zamestnanci[jmeno]

        nove_telefon = input(f"Zadejte nové telefonní číslo ({zamestnanec['telefon']}): ")
        novy_email = input(f"Zadejte nový firemní e-mail ({zamestnanec['email']}): ")
        nova_pozice = input(f"Zadejte nové pracovní zařazení ({zamestnanec['pozice']}): ")
        novy_pokoj = input(f"Zadejte nové číslo pokoje ({zamestnanec['pokoj']}): ")
        novy_skype = input(f"Zadejte nové Skype jméno ({zamestnanec['skype']}): ")

        zamestnanci[jmeno] = {
            "telefon": nove_telefon or zamestnanec["telefon"],
            "email": novy_email or zamestnanec["email"],
            "pozice": nova_pozice or zamestnanec["pozice"],
            "pokoj": novy_pokoj or zamestnanec["pokoj"],
            "skype": novy_skype or zamestnanec["skype"],
            }
    
    elif volba == "5":
      print("Ukončuji program.")
      break

    else:
      print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
  main()
