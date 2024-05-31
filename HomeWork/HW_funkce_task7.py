def je_palindrom(cislo):
  
  # Převedení čísla na řetězec
  cislo_str = str(cislo)

  # Kontrola palindromu
  return cislo_str == cislo_str[::-1]  # Reverzní řetězec

# Příklad použití
cislo = 123321
je_palindrom_cislo = je_palindrom(cislo)
print(f"Číslo {cislo} je palindrom: {je_palindrom_cislo}")

cislo2 = 546645
je_palindrom_cislo = je_palindrom(cislo2)
print(f"Číslo {cislo2} je palindrom: {je_palindrom_cislo}")

cislo3 = 421987
je_palindrom_cislo = je_palindrom(cislo3)
print(f"Číslo {cislo3} je palindrom: {je_palindrom_cislo}")