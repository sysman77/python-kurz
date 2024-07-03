"""
Create a Circle class. Implement the following overloaded operators:

Check if radii of two circles are equal (the == operator);
Compare the lengths of two circles (the operators: >, <, <=,>=);
Proportionally change the circle size by changing its radius (the operators: + - += -=).

Translate:
Vytvořte třídu Circle. Implementujte následující přetížené operátory:

Zkontrolujte, zda jsou poloměry dvou kruhů stejné (operátor ==); 
Porovnejte velikosti dvou kruhů (operátory: >, <, <=, >=); Poměrně změňte velikost kruhu změnou jeho poloměru (operátory: + - += -=).

poloměr -> radius
obvod -> circumference

"""
# import math pro využití funkce Pí
import math

class Circle:
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Kruh, souřadnice ({self.cx}, {self.cy}), Poloměr = {self.radius}")

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.circumference() < other.circumference()

    def __le__(self, other):
        return self.circumference() <= other.circumference()

    def __gt__(self, other):
        return self.circumference() > other.circumference()

    def __ge__(self, other):
        return self.circumference() >= other.circumference()

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.cx, self.cy, self.radius + value)
        raise TypeError("Chyba")

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius < 0:
                raise ValueError("Poloměr nemůže být záporný")
            return Circle(self.cx, self.cy, new_radius)
        raise TypeError("Chyba odčítání")

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        raise TypeError("Chyba sčítání")

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius < 0:
                raise ValueError("Poloměr nemůže být záporný")
            self.radius = new_radius
            return self
        raise TypeError("Chyba odčítání")

    def circumference(self):
        return 2 * math.pi * self.radius

# Zadání
circle1 = Circle(0, 0, 5)
circle2 = Circle(1, 1, 5)
circle3 = Circle(2, 2, 10)

# Kontrola, zda jsou poloměry stejné
print(circle1 == circle2)  # True
print(circle1 == circle3)  # False

# Porovnání obvodů
print(circle1 < circle3)   # True
print(circle1 <= circle3)  # True
print(circle1 > circle3)   # False
print(circle1 >= circle3)  # False

# Změna rozměru kruhů, vytvoření circle4 a circle5
circle1 += 2
circle1.show()  # Kruh, souřadnice (0, 0), poloměr = 7

circle1 -= 3
circle1.show()  # Kruh, souřadnice (0, 0), poloměr = 4

circle4 = circle1 + 6
circle4.show()  # Kruh, souřadnice(0, 0), poloměr = 10

circle5 = circle4 - 4
circle5.show()  # Kruh, souřadnice (0, 0), poloměr = 6

# Ošetření vyjímky pro záporný poloměr
try:
    circle5 -= 10
except ValueError as e:
    print(e)  # Poloměr nemůže být záporný
