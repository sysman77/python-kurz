"""
vytvoř třídu Shape s metodou calculate_area(). Potom vytvoř podtřídy Rectangle, Circle, Triangle atď.,
které překryjí metodu calculate_area() a vypočítají obsah příslušného tvaru.
"""


import math


class Shape:
    def calculate_area(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Příklady použití:
rect = Rectangle(5, 10)
print(f"Obdélník: {rect.calculate_area()}")  # Obdélník: 50

circ = Circle(7)
print(f"Kruh: {circ.calculate_area()}")  # Kruh: 153.93804002589985

tri = Triangle(4, 8)
print(f"Trojúhelník: {tri.calculate_area()}")  # Trojúhelník: 16
