"""
Vytvořte funkci pro zobrazení aktuálního času. Funkce nemá žádné parametry. Ozdobte funkci pomocí jiné funkce
bez použití syntaxe dekorátoru. Možný výstup:

***************************
23:00
***************************

Výsledkem výzdoby jsou zde dvě řady hvězdiček.
"""


import datetime

def get_current_time():
  """
  Vrátí aktuální čas ve formátu HH:MM.
  """
  now = datetime.datetime.now()
  return now.strftime("%H:%M")

def decorate_function(func):
  """
  Dekorační funkce pro vložení hvězdiček před a po volání funkce.
  """
  def wrapper():
    print("***************************")
    result = func()
    print(f"{result}")
    print("***************************")
    return result
  return wrapper

decorated_get_current_time = decorate_function(get_current_time)

# Příklad použití

current_time = decorated_get_current_time()
print(f"Aktuální čas: {current_time}")
