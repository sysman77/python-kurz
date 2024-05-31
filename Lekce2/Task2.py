text_cislo = input("Zadejte číslo: ")
cislo = int(text_cislo)

delitelne = cislo % 7 == 0

if delitelne:
  print(f"Číslo {cislo} je dělitelné 7.")
else:
  print(f"Číslo {cislo} není dělitelné 7.")

