def prvocislo(cislo):
 
  if cislo <= 1:
    return False

  # Zkontroluje zda je prvočíslo
  for delitel in range(2, cislo):
    if cislo % delitel == 0:
      return False

  return True



a = int(input("Zadej číslo:"))
"""
print(prvocislo(13))  # True
print(prvocislo(15))  # False
print(prvocislo(23))  # True
print(prvocislo(1))  # False
"""

print(prvocislo(a))


"""
kontrila prvočísla jinak

 if cislo <= 1:
    return False  # 1 a záporná čísla nejsou prvočísly

  # Kontrola dělitelnosti od 2 do odmocniny čísla
  for delitel in range(2, int(cislo**0.5) + 1):
    if cislo % delitel == 0:
      return False

  return True  # Pokud nenajdeme žádný dělitel, je číslo prvočíslo 


"""