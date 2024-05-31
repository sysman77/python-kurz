def pocet_cifer(cislo):


  # Převedení čísla na řetězec a vypočítání délky
  pocet_cifer = len(str(cislo))

  # Vrácení počtu číslic
  return pocet_cifer

cislo = 123456
pocet_cifer_v_cisle = pocet_cifer(cislo)
print(f"Číslo {cislo} má {pocet_cifer_v_cisle} číslic.")
