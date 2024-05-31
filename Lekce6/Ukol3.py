# Napište rekurzivní funkci, která vytiskne N hvězdiček za sebou, N nastaví uživatel. Na příkladu ilustrujte, jak funkce funguje.

def tiskni_hvezdicky(n):
  
   if n == 0:
    return
   else:
    print("* ", end="")
    tiskni_hvezdicky(n - 1)

h = int(input("Zadej počet hvězdiček:"))
tiskni_hvezdicky(h)