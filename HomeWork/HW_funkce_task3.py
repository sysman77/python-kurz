def tisk_ctverec(delka_strany, symbol, vyplneny=True):

  # Vytvoření řádku symbolu
  radek_symbolu = symbol * delka_strany

  # Vytvoření prázdného čtverce
  if not vyplneny:
    for _ in range(delka_strany):
      print(radek_symbolu)

  # Vytvoření plného čtverce
  else:
    for i in range(delka_strany):
      if i == 0 or i == delka_strany - 1:
        print(radek_symbolu)
      else:
        print(f"{symbol}{' ' * (delka_strany - 2)}{symbol}")


tisk_ctverec(5, "#", True)  # Vytiskne plný čtverec o délce strany 5 s symbolem "#"
tisk_ctverec(5, "* ", False)  # Vytiskne prázdný čtverec o délce strany 5 s symbolem "*"
