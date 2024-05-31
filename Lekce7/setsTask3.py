def rozdil_mesta(sada1, sada2):
  """
  Funkce pro vytvoření sady s městy z první sady, která se nevyskytují ve druhé.

  Argumenty:
    sada1: První sada měst.
    sada2: Druhá sada měst.

  Vrací:
    Sadu obsahující jména měst z první sady, která se nevyskytují ve druhé.
  """

  # Rozdíl sad pomocí operátoru "difference"
  sada_rozdil = sada1 - sada2

  return sada_rozdil

# Příklad použití
sada_mest1 = {"Praha", "Brno", "Ostrava", "Plzeň"}
sada_mest2 = {"České Budějovice", "Plzeň", "Liberec", "Olomouc"}

sada_rozdilnych_mest = rozdil_mesta(sada_mest1, sada_mest2)

print(f"Sada měst z první sady, která se nevyskytují ve druhé sadě: {sada_rozdilnych_mest}")
