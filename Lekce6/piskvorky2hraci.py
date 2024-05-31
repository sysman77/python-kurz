def tah(pole, symbol, x, y):
  """
  Provede tah na herní pole.

  Argumenty:
    pole: Seznam seznamů reprezentující herní pole.
    symbol: Symbol hráče ('X' nebo 'O').
    x: Vodorovná souřadnice tahu (0, 1 nebo 2).
    y: Svislá souřadnice tahu (0, 1 nebo 2).

  Vrací:
    True, pokud byl tah proveden úspěšně, False v opačném případě.
  """
  if 0 <= x < 3 and 0 <= y < 3 and pole[y][x] == '-':
    pole[y][x] = symbol
    return True
  else:
    return False

def vykresli_pole(pole):
  """
  Vykreslí herní pole na konzoli.
  """
  for radek in pole:
    print('| ' + ' | '.join(radek) + ' |')

def vyhodnot_vitezstvi(pole, symbol):
  """
  Zkontroluje, zda je zadaný symbol vítězným.

  Argumenty:
    pole: Seznam seznamů reprezentující herní pole.
    symbol: Symbol hráče ('X' nebo 'O').

  Vrací:
    True, pokud symbol vyhrál, False v opačném případě.
  """
  # Kontrola řádků a sloupců
  for i in range(3):
    if pole[i][0] == symbol and pole[i][1] == symbol and pole[i][2] == symbol:
      return True
    if pole[0][i] == symbol and pole[1][i] == symbol and pole[2][i] == symbol:
      return True

  # Kontrola diagonál
  if pole[0][0] == symbol and pole[1][1] == symbol and pole[2][2] == symbol:
    return True
  if pole[0][2] == symbol and pole[1][1] == symbol and pole[2][0] == symbol:
    return True

  return False

def je_pole_plne(pole):
  """
  Zkontroluje, zda je herní pole plné.

  Argument:
    pole: Seznam seznamů reprezentující herní pole.

  Vrací:
    True, pokud je pole plné, False v opačném případě.
  """
  for radek in pole:
    for bunka in radek:
      if bunka == '-':
        return False
  return True

def main():
  """
  Hlavní funkce hry.
  """
  pole = [['-' for _ in range(3)] for _ in range(3)]
  symbol_hraci = 'X'

  while True:
    vykresli_pole(pole)

    x = int(input("Zadejte vodorovnou souřadnici tahu (0, 1, 2): "))
    y = int(input("Zadejte svislou souřadnici tahu (0, 1, 2): "))

    if not tah(pole, symbol_hraci, x, y):
      print("Neplatný tah. Zkuste znovu.")
      continue

    if vyhodnot_vitezstvi(pole, symbol_hraci):
      vykresli_pole(pole)
      print(f"Hráč {symbol_hraci} vyhrál!")
      break

    if je_pole_plne(pole):
      vykresli_pole(pole)
      print("Remíza!")
      break

    symbol_hraci = 'O' if symbol_hraci == 'X' else 'X'

if __name__ == "__main__":
  main()
