def tiskni_formatovany_text():
  """
  Tato funkce vytiskne formátovaný text s více řádky a odsazením.
  """

  text = """Don´t let the noise of others´ opinions
  drown out your own inner voice"""
  autor = "Steve Jobs"

  # Odsazení textu
  odsazeny_text = "\t" + text.replace("\n", "\n\t")

  # Formátování výstupu
  print(f"""
{odsazeny_text}

                                    {autor}
  """)

tiskni_formatovany_text()
