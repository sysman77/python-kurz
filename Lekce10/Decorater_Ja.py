def ozdobeni(funkce):
    def zabalena_funkce():
        print("***************************")
        funkce()
        print("***************************")
    return zabalena_funkce

def zobraz_aktualni_cas():
    aktualni_cas = ("12:00")
    print(aktualni_cas)

# Ozdobení funkce
ozdobena_funkce = ozdobeni(zobraz_aktualni_cas)

# Volání ozdobené funkce
ozdobena_funkce()