# Python program pro tisk citátu "Být či nebýt" na různé řádky s požadovaným formátováním

# Citát
citát = "Být či nebýt"

# Rozdělení citátu na slova
slova = citát.split()

# Tisk slov na různé řádky s požadovaným formátováním
for index, slovo in enumerate(slova):
  if index == 0:
    # První slovo na samostatný řádek
    print(slovo)
  else:
    # Ostatní slova s odsazením
    print(f"{slovo}")


print("To be\nor not\ntobe")

print()
print("""
To be
or not
to be
"""
    )