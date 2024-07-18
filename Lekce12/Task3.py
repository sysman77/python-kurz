import json

# Funkce pro uložení slovníku do souboru
def save_dict_to_file(data_dict, filename):
    with open(filename, 'w') as file:
        json.dump(data_dict, file)

# Funkce pro načtení slovníku ze souboru
def load_dict_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        data_dict = {}
    return data_dict

# Funkce pro přidání uživatelského jména a hesla
def add_user(data_dict):
    username = input("Zadejte uživatelské jméno: ")
    if username in data_dict:
        print("Uživatelské jméno již existuje.")
    else:
        password = input("Zadejte heslo: ")
        data_dict[username] = password
    return data_dict

# Funkce pro smazání uživatelského jména a hesla
def delete_user(data_dict):
    username = input("Zadejte uživatelské jméno, které chcete smazat: ")
    if username in data_dict:
        del data_dict[username]
        print(f"Uživatelské jméno '{username}' bylo smazáno.")
    else:
        print("Uživatelské jméno nebylo nalezeno.")
    return data_dict

# Funkce pro vyhledání uživatelského jména
def search_user(data_dict):
    username = input("Zadejte uživatelské jméno, které chcete vyhledat: ")
    if username in data_dict:
        print(f"Heslo pro uživatelské jméno '{username}' je: {data_dict[username]}")
    else:
        print("Uživatelské jméno nebylo nalezeno.")

# Funkce pro editaci hesla uživatelského jména
def edit_user(data_dict):
    username = input("Zadejte uživatelské jméno, jehož heslo chcete změnit: ")
    if username in data_dict:
        new_password = input("Zadejte nové heslo: ")
        data_dict[username] = new_password
        print(f"Heslo pro uživatelské jméno '{username}' bylo změněno.")
    else:
        print("Uživatelské jméno nebylo nalezeno.")
    return data_dict

# Hlavní program s menu
def main():
    filename = 'user_data.json'
    data_dict = load_dict_from_file(filename)

    while True:
        print("\nMenu:")
        print("1. Přidání uživatelských dat")
        print("2. Smazání uživatelských dat")
        print("3. Vyhledání uživatelských dat")
        print("4. Editace uživatelských dat")
        print("5. Uložení dat")
        print("6. Načtení dat")
        print("7. Konec")

        choice = input("Vyberte akci (1-7): ")

        if choice == '1':
            data_dict = add_user(data_dict)
        elif choice == '2':
            data_dict = delete_user(data_dict)
        elif choice == '3':
            search_user(data_dict)
        elif choice == '4':
            data_dict = edit_user(data_dict)
        elif choice == '5':
            save_dict_to_file(data_dict, filename)
            print("Data byla uložena.")
        elif choice == '6':
            data_dict = load_dict_from_file(filename)
            print("Data byla načtena.")
        elif choice == '7':
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()