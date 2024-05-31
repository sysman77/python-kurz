cislo = int(input("Zadejte číslo: "))

if cislo % 2 == 0:
  vysledek = "Sudé"
else:
  vysledek = "Liché"

print(f"Zadané číslo {cislo} je {vysledek}.")


"""
if cislo % 2: # True, False
  vysledek = "Liché"
else:
  vysledek = "Sudé"

"""


""" varianta
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num)) 

"""