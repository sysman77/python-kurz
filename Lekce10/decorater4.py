"""
Vytvořte aplikaci pro výrobu pizzy. Každá pizza má jiné ingredience. Pomocí dekoratérů vytvořte různé pizzy:

Margarita;
Čtyři sýry;
Náladový;
Havajský.

"""

# Definice základní funkce pro výrobu pizzy
def vyrob_pizzu():
    print("Těsto")

# Dekorátor pro pizzu Margarita
def margarita(funkce):
    def zabalena_funkce():
        funkce()
        print("Rajčatová omáčka")
        print("Mozzarella")
        print("Bazalka")
    return zabalena_funkce

# Dekorátor pro pizzu Čtyři sýry
def ctyri_syry(funkce):
    def zabalena_funkce():
        funkce()
        print("Rajčatová omáčka")
        print("Mozzarella")
        print("Gorgonzola")
        print("Parmezán")
        print("Emmental")
    return zabalena_funkce

# Dekorátor pro pizzu Náladový
def naladovy(funkce):
    def zabalena_funkce():
        funkce()
        print("Rajčatová omáčka")
        print("Mozzarella")
        print("Pepperoni")
        print("Jalapeños")
        print("Olivy")
    return zabalena_funkce

# Dekorátor pro pizzu Havajský
def havajsky(funkce):
    def zabalena_funkce():
        funkce()
        print("Rajčatová omáčka")
        print("Mozzarella")
        print("Šunka")
        print("Ananas")
    return zabalena_funkce

# Použití dekorátorů pro vytvoření různých pizz
@havajsky
def havajska_pizza():
    vyrob_pizzu()

@naladovy
def naladova_pizza():
    vyrob_pizzu()

@ctyri_syry
def pizza_ctyri_syry():
    vyrob_pizzu()

@margarita
def pizza_margarita():
    vyrob_pizzu()

# Výroba a výpis různých pizz
print("Výroba pizzy Margarita:")
pizza_margarita()
print("\nVýroba pizzy Čtyři sýry:")
pizza_ctyri_syry()
print("\nVýroba pizzy Náladový:")
naladova_pizza()
print("\nVýroba pizzy Havajský:")
havajska_pizza()

"""
V tomto kódu:

vyrob_pizzu je základní funkce, která vypíše "Těsto".
Každý dekorátor (margarita, ctyri_syry, naladovy, havajsky) přidá specifické ingredience k základní funkci vyrob_pizzu.
Použitím syntaxe dekorátoru @ před definicí funkce pizzy (havajska_pizza, naladova_pizza, pizza_ctyri_syry, 
pizza_margarita) aplikujeme příslušné dekorátory na základní funkci vyrob_pizzu.
Zavoláním funkcí pizza_margarita, pizza_ctyri_syry, naladova_pizza a havajska_pizza se vypíší ingredience pro 
danou pizzu včetně těsta.
"""