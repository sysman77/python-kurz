"""
Vytvořte třídu pro nalezení největšího a nejmenšího ze čtyř argumentů, průměru a faktoriálu.
Implementujte tuto funkci jako statické metody.
"""

class StatsCalculator:
  """
  Třída pro statistické operace s argumenty.
  """

  @staticmethod
  def find_max(a, b, c, d):
    """
    Najde maximum ze čtyř argumentů.
    """
    maximum = max(a, b, c, d)
    return maximum

  @staticmethod
  def find_min(a, b, c, d):
    """
    Najde minimum ze čtyř argumentů.
    """
    minimum = min(a, b, c, d)
    return minimum

  @staticmethod
  def calculate_average(a, b, c, d):
    """
    Vypočítá průměr ze čtyř argumentů.
    """
    average = (a + b + c + d) / 4
    return average

  @staticmethod
  def calculate_factorial(number):
    """
    Vypočítá faktoriál zadaného čísla.
    """
    if number < 0:
      raise ValueError("Faktoriál záporného čísla neexistuje.")

    if number == 0:
      return 1

    product = 1
    for i in range(1, number + 1):
      product *= i

    return product


# Příklad použití

max_value = StatsCalculator.find_max(10, 20, 30, 40)
min_value = StatsCalculator.find_min(10, 20, 30, 40)
avg_value = StatsCalculator.calculate_average(10, 20, 30, 40)
factorial_value = StatsCalculator.calculate_factorial(5)

print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Průměr: {avg_value}")
print(f"Faktoriál (5): {factorial_value}")

"""
V tomto kódu:

Třída StatsCalculator obsahuje statické metody:
find_max(a, b, c, d): Vrátí maximum ze čtyř zadaných argumentů.
find_min(a, b, c, d): Vrátí minimum ze čtyř zadaných argumentů.
calculate_average(a, b, c, d): Vypočítá průměr ze čtyř zadaných argumentů.
calculate_factorial(number): Vypočítá faktoriál zadaného čísla. Kontroluje zadané číslo a vrací výsledek.
V příkladu použití se volájí statické metody s ukázkovými hodnotami a výsledky se tisknou.
Tato třída umožňuje provádět základní statistické operace s argumenty bez nutnosti vytvářet instance. 
Statické metody jsou dostupné přímo z třídy a usnadňují tak jejich opakované použití.
"""