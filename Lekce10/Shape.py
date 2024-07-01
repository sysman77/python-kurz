"""
vytvoř třídu Shape s metodou calculate_area(). Potom vytvoř podtřídy Rectangle, Circle, Triangle atď.,
které překryjí metodu calculate_area() a vypočítají obsah příslušného tvaru.
"""
class Shape:
  """
  Základní třída pro tvary.
  """

  def __init__(self):
    pass

  def calculate_area(self):
    """
    Abstraktní metoda pro výpočet plochy.
    Musí být přepsána v podtřídách.
    """
    raise NotImplementedError("Metoda calculate_area() není implementována.")


class Rectangle(Shape):
  """
  Třída pro obdélníky.
  """

  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width

  def calculate_area(self):
    """
    Vypočítá plochu obdélníku.
    """
    return self.length * self.width


class Circle(Shape):
  """
  Třída pro kruhy.
  """

  def __init__(self, radius):
    super().__init__()
    self.radius = radius

  def calculate_area(self):
    """
    Vypočítá plochu kruhu.
    """
    return 3.1415 * self.radius * self.radius


class Triangle(Shape):
  """
  Třída pro trojúhelníky.
  """

  def __init__(self, base, height):
    super().__init__()
    self.base = base
    self.height = height

  def calculate_area(self):
    """
    Vypočítá plochu trojúhelníku.
    """
    return 0.5 * self.base * self.height


# Příklad použití

rectangle = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(6, 4)

print(f"Plocha obdélníku: {rectangle.calculate_area()}")
print(f"Plocha kruhu: {circle.calculate_area()}")
print(f"Plocha trojúhelníku: {triangle.calculate_area()}")
