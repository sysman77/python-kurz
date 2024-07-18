def save_text_to_file():
    try:
        # Získání názvu souboru od uživatele
        filename = input("Zadejte název souboru (s příponou): ")

        # Získání textu od uživatele
        text_to_save = input("Zadejte text, který chcete uložit do souboru: ")

        # Otevření souboru pro zápis
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text_to_save)

        print(f"Text byl úspěšně uložen do souboru '{filename}'.")

    except Exception as e:
        # Zachycení a zobrazení jakékoli výjimky
        print(f"Při ukládání textu došlo k chybě: {e}")


def read_text_from_file():
    try:
        # Získání názvu souboru od uživatele
        filename = input("Zadejte název souboru (s příponou), který chcete číst: ")

        # Otevření souboru pro čtení
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        print(f"Obsah souboru '{filename}':")
        print(content)

    except Exception as e:
        # Zachycení a zobrazení jakékoli výjimky
        print(f"Při čtení souboru došlo k chybě: {e}")


def append_text_to_file():
    try:
        # Získání názvu souboru od uživatele
        filename = input("Zadejte název souboru (s příponou), do kterého chcete přidat text: ")

        # Získání textu od uživatele
        text_to_append = input("Zadejte text, který chcete přidat do souboru: ")

        # Otevření souboru pro přidávání (append)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text_to_append)

        print(f"Text byl úspěšně přidán do souboru '{filename}'.")

    except Exception as e:
        # Zachycení a zobrazení jakékoli výjimky
        print(f"Při přidávání textu do souboru došlo k chybě: {e}")


# Menu pro výběr operace
def main():
    while True:
        print("\nVyberte operaci:")
        print("1. Uložit text do nového souboru")
        print("2. Číst text ze souboru")
        print("3. Přidat text do existujícího souboru")
        print("4. Konec")

        choice = input("Zadejte číslo operace: ")

        if choice == '1':
            save_text_to_file()
        elif choice == '2':
            read_text_from_file()
        elif choice == '3':
            append_text_to_file()
        elif choice == '4':
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Zavolání hlavní funkce
main()
