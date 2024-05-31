# Získání délek úhlopříček od uživatele
uhlopricka1 = float(input("Zadejte délku první úhlopříčky (v cm): "))
uhlopricka2 = float(input("Zadejte délku druhé úhlopříčky (v cm): "))

# Výpočet plochy
plocha = (uhlopricka1 * uhlopricka2) / (2 * 4)  # Vzorce pro výpočet plochy diamantu

# Zobrazení výsledku
print(f"Plocha diamantu s úhlopříčkami {uhlopricka1:.2f} cm a {uhlopricka2:.2f} cm je: {plocha:.2f} cm čtverečních")