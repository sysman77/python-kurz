def tiskni_caru(delka, smer, symbol):
  """
  Tato funkce vytiskne vodorovnou nebo svislou čáru zadané délky vytvořenou ze zadaného symbolu.

  Argumenty:
    delka: Celková délka čáry.
    smer: Směr čáry ('v' pro svislou, 'h' pro vodorovnou).
    symbol: Symbol, ze kterého se čára skládá.

  """

  if smer.lower() == 'v':
    # Svislá čára
    for _ in range(delka):
      print(symbol)
  elif smer.lower() == 'h':
    # Vodorovná čára
    print(symbol * delka)
  else:
    raise ValueError(f"Neplatný směr: {smer}. Možné hodnoty jsou 'v' a 'h'.")

# Příklad použití
delka = int(input("Zadejte délku čáry: "))
smer = str(input("Zadejte směr čáry h/v: "))
symbol = str(input("Zadejte znak: "))

tiskni_caru(delka, smer, symbol)


"""
def task3(length, symbol="x", direction="horizontal"):
    for _ in range(length):
        if direction == "horizontal":
            print(symbol, end=" ")

        if direction == "vertical":
            print(symbol)


#task3(4)
#task3(4, "#")
#task3(4, symbol="#")
#task3(4, direction="vertical")
task3(4, direction="vertical", symbol="F") 

"""

"""
VERTICAL = "vertical"
HORIZONTAL = "horizontal"
def task3_version3(length, symbol="x", direction=HORIZONTAL):
    end_line = " "
    if direction == VERTICAL:
        end_line = "\n"
        
    for _ in range(length):
        print(symbol, end=end_line) 
"""
