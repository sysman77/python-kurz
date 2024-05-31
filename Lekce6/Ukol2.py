# Napište rekurzivní funkci, která vypočítá součet všech čísel v rozsahu od a do b. Uživatel zadá a a b. Na příkladu ilustrujte, jak funkce funguje.

def soucet_v_rozsahu(a, b):
   if a > b:
    return 0
   else:
    return a + soucet_v_rozsahu(a + 1, b)

a = int(input("Zadej nižší číslo rozsahu: "))
b = int(input("Zadej vyšší číslo rozsahu: "))
soucet = soucet_v_rozsahu(a, b)
print("Součet čísel zadaném rozsahu je:",soucet)  # pro a=1 a b=10, Vypíše 55