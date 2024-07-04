# Seznam n-tic pro ukládání dat
pokuty = []

# Příklad inicializace dat
pokuty.append(('123456/7890', 'Jan', 'Novák', 'Dlouhá 123', 'Praha', 'Rychlostní přestupek', 'Překročení povolené rychlosti o 30 km/h', 2000.0))
pokuty.append(('987654/3210', 'Eva', 'Svobodová', 'Krátká 456', 'Brno', 'Parkovací přestupek', 'Parkování na chodníku', 1000.0))

def pridej_osobu(osobni_kod, jmeno, prijmeni, adresa, mesto):
    pokuty.append((osobni_kod, jmeno, prijmeni, adresa, mesto, None, None, None))
    print(f"Osoba s osobním kódem {osobni_kod} byla úspěšně přidána.")

# Příklad použití
pridej_osobu('555555/1234', 'Petr', 'Nový', 'Hlavní 789', 'Ostrava')


def pridej_trest(osobni_kod, typ_trestu, popis, castka):
    for i, pokuta in enumerate(pokuty):
        if pokuta[0] == osobni_kod:
            pokuty[i] = pokuta[:5] + (typ_trestu, popis, castka)
            print(f"Nový trest byl úspěšně přidán osobě s osobním kódem {osobni_kod}.")
            return
    print(f"Osoba s osobním kódem {osobni_kod} nebyla nalezena.")

# Příklad použití
pridej_trest('555555/1234', 'Alkoholový test', 'Odmítnutí provedení alkoholového testu', 3000.0)

def smaz_trest(osobni_kod, typ_trestu):
    for i, pokuta in enumerate(pokuty):
        if pokuta[0] == osobni_kod and pokuta[5] == typ_trestu:
            pokuty[i] = pokuta[:5] + (None, None, None)
            print(f"Trest '{typ_trestu}' byl smazán pro osobu s osobním kódem {osobni_kod}.")
            return
    print(f"Trest '{typ_trestu}' pro osobu s osobním kódem {osobni_kod} nebyl nalezen.")

# Příklad použití
smaz_trest('555555/1234', 'Alkoholový test')

def nahrad_informace(osobni_kod, jmeno=None, prijmeni=None, adresa=None, mesto=None):
    for i, pokuta in enumerate(pokuty):
        if pokuta[0] == osobni_kod:
            new_pokuta = list(pokuta)
            if jmeno:
                new_pokuta[1] = jmeno
            if prijmeni:
                new_pokuta[2] = prijmeni
            if adresa:
                new_pokuta[3] = adresa
            if mesto:
                new_pokuta[4] = mesto
            pokuty[i] = tuple(new_pokuta)
            print(f"Informace o osobě s osobním kódem {osobni_kod} byly aktualizovány.")
            return
    print(f"Osoba s osobním kódem {osobni_kod} nebyla nalezena.")

# Příklad použití
nahrad_informace('555555/1234', prijmeni='Novotný')

def tiskni_databazi():
    print("Úplná tištěná kopie databáze:")
    for pokuta in pokuty:
        print(pokuta)

# Příklad použití
tiskni_databazi()

def tiskni_podle_kodu(osobni_kod):
    print(f"Tištěná kopie dat pro osobu s osobním kódem '{osobni_kod}':")
    for pokuta in pokuty:
        if pokuta[0] == osobni_kod:
            print(pokuta)

# Příklad použití
tiskni_podle_kodu('555555/1234')

def tiskni_podle_typu_trestu(typ_trestu):
    print(f"Tištěná kopie dat pro trest typu '{typ_trestu}':")
    for pokuta in pokuty:
        if pokuta[5] == typ_trestu:
            print(pokuta)

# Příklad použití
tiskni_podle_typu_trestu('Rychlostní přestupek')

def tiskni_podle_mesta(mesto):
    print(f"Tištěná kopie dat pro město '{mesto}':")
    for pokuta in pokuty:
        if pokuta[4] == mesto:
            print(pokuta)

# Příklad použití
tiskni_podle_mesta('Praha')
