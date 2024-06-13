strings = ["První řádek", "Druhý řádek", "Třetí řádek", "Čtvrtý řádek"]

output_file = 'data/reversed_strings_output.txt'

try:
    # Otevření výstupního souboru pro zápis
    with open(output_file, 'w', encoding='utf-8') as f_out:
        # Zápis každého řetězce na samostatný řádek, ale v obráceném pořadí
        for string in reversed(strings):
            f_out.write(string + '\n')

    print(f'Úspěšně zapsáno do souboru {output_file}')

except IOError:
    print(f'Problém s čtením/zápisem do souboru.')
