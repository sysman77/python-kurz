import json


# Funkce pro načtení dat ze souboru
def load_data(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Funkce pro uložení dat do souboru
def save_data(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Funkce pro přidání nové restaurace
def add_restaurant(data):
    name = input("Zadejte název restaurace: ")
    specialization = input("Zadejte specializaci restaurace: ")
    address = input("Zadejte adresu restaurace: ")
    web = input("Zadejte webovou stránku restaurace: ")
    phone = input("Zadejte telefonní číslo restaurace: ")

    new_restaurant = {
        "Název": name,
        "Specializace": specialization,
        "Adresa": address,
        "Web": web,
        "Telefonní číslo": phone
    }

    data.append(new_restaurant)
    save_data(data, "restaurants.json")
    print("Restaurace byla úspěšně přidána.")


# Funkce pro výpis všech restaurací
def list_restaurants(data):
    if not data:
        print("Seznam restaurací je prázdný.")
    else:
        for index, restaurant in enumerate(data, start=1):
            print(
                f"{index}. {restaurant['Název']}, {restaurant['Specializace']}, {restaurant['Adresa']}, {restaurant['Web']}, {restaurant['Telefonní číslo']}")


# Funkce pro odstranění restaurace
def delete_restaurant(data):
    list_restaurants(data)
    if data:
        index = int(input("Zadejte číslo restaurace, kterou chcete odstranit: ")) - 1
        if 0 <= index < len(data):
            removed = data.pop(index)
            save_data(data, "restaurants.json")
            print(f"Restaurace {removed['Název']} byla úspěšně odstraněna.")
        else:
            print("Neplatné číslo restaurace.")


# Hlavní menu
def menu():
    data = load_data("restaurants.json")

    while True:
        print("\nMenu:")
        print("1. Přidat restauraci")
        print("2. Vypsat restaurace")
        print("3. Smazat restauraci")
        print("4. Ukončit")

        choice = input("Vyberte možnost: ")

        if choice == "1":
            add_restaurant(data)
        elif choice == "2":
            list_restaurants(data)
        elif choice == "3":
            delete_restaurant(data)
        elif choice == "4":
            print("Ukončení programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


# Spuštění menu
menu()
