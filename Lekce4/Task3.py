text = "Asldkjlsdn aksjhcjnů 6546ds1t6 w65d1fw w54e65f1dasdasRVuBiuI ljhAJ !AD ASD!"

print(text)

# začáteční písmena velká
slova = text.split()
for i in range(len(slova)):
    slova[i] = slova[i].capitalize()

text_velka = " ".join(slova)

print(f"Text s velkými začátečními písmeny: {text_velka}")


# celkový počet vykřičníků

pocet_vykricniku = 0

for znak in text:
    if znak == "!":
        pocet_vykricniku += 1

print(f"Počet vykřičníků v textu: {pocet_vykricniku}")
print(text.count("!")) # to stejné jinak


# celkový počet čísel
pocet_cisel = 0

for znak in text:
    if znak.isdigit():
        pocet_cisel += 1

print(f"Počet čísel v textu: {pocet_cisel}")

# Kolikrát se v textu objeví interpunční znménko


pocet_interpunkce = 0


for znak in text:
  if znak in ",.;!?":
    pocet_interpunkce += 1


print(f"Počet interpunkčních znamének v textu: {pocet_interpunkce}")
    

