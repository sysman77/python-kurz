def sjednot_mesta(sada1, sada2):
  """
  Funkce pro sjednocení dvou sad měst do třetí sady.

  Argumenty:
    sada1: První sada měst.
    sada2: Druhá sada měst.

  Vrací:
    Třetí sada obsahující jména měst z obou sad (bez duplicit).
  """

  # Sjednocení sad pomocí operátoru "union"
  sada_sjednocena = sada1 | sada2

  # Konverze na seznam pro odstranění duplicit
  seznam_sjednocenych_mest = list(sada_sjednocena)

  # Odstranění duplicitních položek
  for i in range(len(seznam_sjednocenych_mest) - 1, -1, -1):
    if seznam_sjednocenych_mest.count(seznam_sjednocenych_mest[i]) > 1:
      del seznam_sjednocenych_mest[i]

  # Konverze zpět na sadu
  sada_sjednocena = set(seznam_sjednocenych_mest)

  return sada_sjednocena

# Příklad použití
sada_mest1 = {"Praha", "Brno", "Ostrava", "Plzeň"}
sada_mest2 = {"České Budějovice", "Plzeň", "Liberec", "Olomouc"}

sjednocena_sada_mest = sjednot_mesta(sada_mest1, sada_mest2)

print(f"Sjednocená sada měst: {sjednocena_sada_mest}")
