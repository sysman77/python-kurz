from random import randint

def drunkman_simulator(size, steps, output=False):
  """
  Simulace opilcova pohybu mezi domovem a hospodou.

  https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html

  Argumenty:
    size: Vzdálenost mezi domovem a hospodou.
    steps: Počet kroků do opilcova usnutí (maximální délka simulace).
    output: Volitelný parametr, který určuje, zda se má simulace vypisovat na konzoli (výchozí hodnota je False).

  Vrací:
    True, pokud opilec dojde domů, False v opačném případě.
  """

  position = size // 2
  direction = 1

  for _ in range(steps):
    step = randint(-1, 1)
    position += step * direction

    if position == 0:
      # Došel domů
      if output:
        print("Opilec se dobelhal domů!")
      return True
    elif position == size:
      # Došel do hospody
      if output:
        print("Opilec se opět dopotácel do hospody!")
      return False

  # Došel maximální počet kroků
  if output:
    print("Simulace skončila po maximálním počtu kroků.")
  return False

def drunkman_analysis(size, steps, count):
  """
  Analyzuje simulaci opilce a vypisuje procentuální úspěšnost dojití domů.

  Argumenty:
    size: Vzdálenost mezi domovem a hospodou.
    steps: Počet kroků do opilcova usnutí (maximální délka simulace).
    count: Počet simulací k provedení.
  """

  success_count = 0
  for _ in range(count):
    if drunkman_simulator(size, steps):
      success_count += 1

  success_rate = success_count / count * 100
  print(f"Opilec se dobelhal domů v {success_rate:.1f} % případů.")

# Ukázkový výstup
drunkman_analysis(10, 100, 100)
# Opilec se dobelhal domů v 45.0 % případů.
