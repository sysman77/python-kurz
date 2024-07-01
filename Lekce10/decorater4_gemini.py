def pizza_base(func):
  """
  Dekorační funkce pro přidání základu pizzy.
  """
  def wrapper(ingredients):
    return f"{func(ingredients)} na tenkém těstě s rajčatovou omáčkou a mozzarellou."
  return wrapper

def add_cheese(ingredients):
  """
  Přidá sýr na pizzu.
  """
  return f"{ingredients} se sýrem."

def add_tomatoes(ingredients):
  """
  Přidá rajčata na pizzu.
  """
  return f"{ingredients} s rajčaty."

def add_pineapple(ingredients):
  """
  Přidá ananas na pizzu.
  """
  return f"{ingredients} s ananasem."

def add_ham(ingredients):
  """
  Přidá šunku na pizzu.
  """
  return f"{ingredients} se šunkou."

def add_mushrooms(ingredients):
  """
  Přidá houby na pizzu.
  """
  return f"{ingredients} s houbami."

# Definice pizz

@pizza_base
@add_tomatoes
@add_cheese
def pizza_margherita():
  """
  Ingredience pro pizzu Margherita.
  """
  return "Bazalka"

@pizza_base
@add_cheese
def pizza_quattro_formaggi():
  """
  Ingredience pro pizzu Čtyři sýry.
  """
  return "Mozzarella, Gorgonzola, Parmigiano Reggiano, Fontina"

@pizza_base
@add_tomatoes
@add_cheese
@add_ham
@add_mushrooms
def pizza_capricciosa():
  """
  Ingredience pro pizzu Náladový.
  """
  return ""

@pizza_base
@add_tomatoes
@add_cheese
@add_pineapple
@add_ham
def pizza_hawaii():
  """
  Ingredience pro pizzu Havajský.
  """
  return ""

# Příklad použití

pizza_margherita_description = pizza_margherita()
pizza_quattro_formaggi_description = pizza_quattro_formaggi()
pizza_capricciosa_description = pizza_capricciosa()
pizza_hawaii_description = pizza_hawaii()

print(f"Pizza Margherita: {pizza_margherita_description}")
print(f"Pizza Čtyři sýry: {pizza_quattro_formaggi_description}")
print(f"Pizza Náladový: {pizza_capricciosa_description}")
print(f"Pizza Havajský: {pizza_hawaii_description}")

"""
V tomto kódu:

Dekorátory pizza_base, add_cheese, add_tomatoes, add_pineapple, add_ham, add_mushrooms se používají k přidávání 
ingrediencí na pizzu.
Každá pizza má vlastní funkci, která definuje její ingredience.
Dekorátory se aplikují na funkce pizz v pořadí, v jakém se používají.
Funkce pizza_base se aplikuje jako první a přidává základ pizzy.
Následují dekorátory pro přidávání dalších ingrediencí.
Výsledný popis pizzy se skládá ze všech přidaných ingrediencí.
Na konci kódu se vytvoří popisy pizz a vytisknou se.
Tento příklad ukazuje, jak lze dekorátory využít k elegantnímu a modulárnímu vytvoření různých pizz s různými 
ingrediencemi. Dekorátory usnadňují přidávání a odebírání ingrediencí a udržují kód organizovaný a přehledný.
"""