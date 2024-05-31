# Získání hodnot od uživatele
plat = float(input("Zadejte svůj měsíční plat: "))
platba_uver = float(input("Zadejte měsíční platbu za úvěr: "))
platba_sluzby = float(input("Zadejte platbu za služby: "))

# Výpočet zůstatku
zustatek = plat - platba_uver - platba_sluzby

# Zobrazení výsledku
print(f"Po odečtení všech plateb vám zbyde {zustatek:.2f} Kč.")