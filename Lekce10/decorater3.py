import datetime

# Definice dekorátoru
def ozdobeni_hvezdicky(funkce):
    def zabalena_funkce():
        print("***************************")
        funkce()
        print("***************************")
    return zabalena_funkce

# Použití dekorátoru pomocí syntaxe dekorátoru
@ozdobeni_hvezdicky
def zobraz_aktualni_cas():
    aktualni_cas = datetime.datetime.now().strftime("%H:%M")
    print(aktualni_cas)

# Volání ozdobené funkce
zobraz_aktualni_cas()
