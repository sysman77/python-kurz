# Napište rekurzivní funkci k nalezení mocniny čísla

def mocnina(cislo, exponent):

  if exponent == 0:
    return 1
  else:
    return cislo * mocnina(cislo, exponent - 1)


vysledek = mocnina(2, 5) # 2 na 5
print(vysledek)  # Vypíše 32

vysledek2 = mocnina(3, 3) #  3 na 3
print(vysledek2)  # Vypíše 27