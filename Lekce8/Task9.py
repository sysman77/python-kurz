def count_characters(filename):
    try:
        # Otevření vstupního souboru pro čtení
        with open(filename, 'r', encoding='utf-8') as f:
            # Přečtení celého obsahu souboru do proměnné text
            text = f.read()
            # Vypočítání počtu znaků v textu
            char_count = len(text)

        return char_count

    except FileNotFoundError:
        print(f'Soubor {filename} neexistuje.')
    except IOError:
        print(f'Problém s čtením souboru {filename}.')

# Použití funkce pro výpočet počtu znaků
input_file = 'data/text.txt'
characters_count = count_characters(input_file)

if characters_count is not None:
    print(f'Počet znaků ve souboru {input_file}: {characters_count}')
