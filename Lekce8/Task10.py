def count_lines(filename):
    try:
        # Otevření vstupního souboru pro čtení
        with open(filename, 'r', encoding='utf-8') as f:
            # Čtení souboru a výpočet počtu řádků
            line_count = sum(1 for line in f)

        return line_count

    except FileNotFoundError:
        print(f'Soubor {filename} neexistuje.')
    except IOError:
        print(f'Problém s čtením souboru {filename}.')

# Použití funkce pro výpočet počtu řádků
input_file = 'data/text.txt'
lines_count = count_lines(input_file)

if lines_count is not None:
    print(f'Počet řádků ve souboru {input_file}: {lines_count}')
