db = {  "Albania": "Tirana",
  "Andorra": "Andorra la Vella",
  "Austria": "Vienna",
  "Belarus": "Minsk",
  "Belgium": "Brussels",
  "Bosnia and Herzegovina": "Sarajevo",
  "Bulgaria": "Sofia",
  "Croatia": "Zagreb",
  "Cyprus": "Nicosia",
  "Czech Republic": "Prague",
  "Denmark": "Copenhagen",
  "Estonia": "Tallinn",
  "Finland": "Helsinki",
  "France": "Paris",
  "Germany": "Berlin"}

def add_country():
    country = input("Zadejte název země: ")
    capital = input("Zadejte hlavní město: ")
    if country in db:
        print(f"{country} už je v seznamu.")
    else:
        db[country] = capital
        print(f"Přidáno: {country} -> {capital}")

def remove_country():
    country = input("Zadejte název země: ")
    if country in db:
        del db[country]
        print(f"{country} bylo odstraněno ze seznamu.")
    else:
        print(f"{country} nebylo nalezeno v seznamu.")

def find_capital():
    country = input("Zadejte název země: ")
    capital = db.get(country, "Země nebyla nalezena v seznamu.")
    print(f"Hlavní město země {country} je {capital}")

def replace_capital():
    country = input("Zadejte název země: ")
    if country in db:
        new_capital = input("Zadejte nové hlavní město: ")
        db[country] = new_capital
        print(f"Pro {country} bylo hlavní město nahrazeno novým: {new_capital}")
    else:
        print(f"{country} nebylo nalezeno v seznamu.")

def print_all():
    if db:
        for country, capital in db.items():
            print(f"{country} -> {capital}")
    else:
        print("Seznam je prázdný.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Přidat zemi a hlavní město")
        print("2. Odstranit zemi")
        print("3. Vyhledat hlavní město")
        print("4. Nahradit hlavní město")
        print("5. Vypsat všechny země a hlavní města")
        print("6. Konec")
        
        choice = input("Vyberte možnost (1-6): ")
        
        if choice == '1':
            add_country()
        elif choice == '2':
            remove_country()
        elif choice == '3':
            find_capital()
        elif choice == '4':
            replace_capital()
        elif choice == '5':
            print_all()
        elif choice == '6':
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Spuštění menu
menu()
