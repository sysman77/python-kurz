# Získání čísel od uživatele
cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))

# Porovnání čísel a určení většího
# splní se právě jedna
if cislo1 > cislo2:
    print("První číslo je větší")
elif cislo1 == cislo2:
    print("Obě čísla jsou stejná")
else:
    print("Druhé číslo je větší")

"""" varianta 

# Porovnání čísel a určení většího

# splní se žádná až všechny

if cislo1 > cislo2:
    print("První číslo je větší")

if cislo1 == cislo2:
    print("Obě čísla jsou stejná")

if cislo < cislo2:
    print("Druhé číslo je větší")


"""