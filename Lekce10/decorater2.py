import datetime

def ozdobeni_hvezdicky(funkce):
    def zabalena_funkce():
        print("***************************")
        funkce()
        print("***************************")
    return zabalena_funkce

def ozdobeni_pomlcky(funkce):
    def zabalena_funkce():
        print("---------------------------")
        funkce()
        print("---------------------------")
    return zabalena_funkce

def zobraz_aktualni_cas():
    aktualni_cas = datetime.datetime.now().strftime("%H:%M")
    print(aktualni_cas)

# Ozdobení funkce oběma dekorátory
ozdobena_funkce_hvezdicky = ozdobeni_hvezdicky(zobraz_aktualni_cas)
ozdobena_funkce_hvezdicky_a_pomlcky = ozdobeni_pomlcky(ozdobena_funkce_hvezdicky)

# Volání dvojitě ozdobené funkce
ozdobena_funkce_hvezdicky_a_pomlcky()
