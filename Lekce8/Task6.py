input_file = 'data/text.txt'
output_file = 'data/hvezdicky.txt'

# Funkce pro převrácení znaků * a &
def swap_chars(line):
    swapped_line = []
    for char in line:
        if char == '*':
            swapped_line.append('&')
        elif char == '&':
            swapped_line.append('*')
        else:
            swapped_line.append(char)
    return ''.join(swapped_line)

try:
    # Otevření vstupního souboru pro čtení
    with open(input_file, 'r', encoding='utf-8') as f_in:
        # Otevření výstupního souboru pro zápis
        with open(output_file, 'w', encoding='utf-8') as f_out:
            # Pro každý řádek vstupního souboru provedeme substituci a zapíšeme do výstupního souboru
            for line in f_in:
                swapped_line = swap_chars(line)
                f_out.write(swapped_line)

    print(f'Úspěšně zapsáno do souboru {output_file}')

except FileNotFoundError:
    print(f'Soubor {input_file} neexistuje.')
except IOError:
    print(f'Problém s čtením/zápisem souboru.')
