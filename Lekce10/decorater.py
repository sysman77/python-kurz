import datetime

def ozdobeni(funkce):
    def zabalena_funkce():
        print("***************************")
        funkce()
        print("***************************")
    return zabalena_funkce

def zobraz_aktualni_cas():
    aktualni_cas = datetime.datetime.now().strftime("%H:%M")
    print(aktualni_cas)

# Ozdobení funkce
ozdobena_funkce = ozdobeni(zobraz_aktualni_cas)

# Volání ozdobené funkce
ozdobena_funkce()
