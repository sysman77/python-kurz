def tiskni_formatovany_text():
  """
  Tato funkce vytiskne formátovaný text s více řádky a odsazením.
  """

  text = """Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself."""
  autor = "Bill Gates"

  # Odsazení textu
  odsazeny_text = "\t" + text.replace("\n", "\n\t")

  # Formátování výstupu
  print(f"""
{odsazeny_text}

                                    {autor}
  """)

tiskni_formatovany_text()