import math

class Circle:
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Circle: Center at ({self.cx}, {self.cy}), Radius = {self.radius}")

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
        raise TypeError("Unsupported type for addition")

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius < 0:
                raise ValueError("Radius cannot be negative")
            return Circle(self.cx, self.cy, new_radius)
        raise TypeError("Unsupported type for subtraction")

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        raise TypeError("Unsupported type for addition")

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius < 0:
                raise ValueError("Radius cannot be negative")
            self.radius = new_radius
            return self
        raise TypeError("Unsupported type for subtraction")

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circle1 = Circle(0, 0, 5)
circle2 = Circle(1, 1, 5)
circle3 = Circle(2, 2, 10)

# Check if radii are equal
print(circle1 == circle2)  # True
print(circle1 == circle3)  # False

# Compare circumferences
print(circle1 < circle3)   # True
print(circle1 <= circle3)  # True
print(circle1 > circle3)   # False
print(circle1 >= circle3)  # False

# Change size of circle
circle1 += 2
circle1.show()  # Circle: Center at (0, 0), Radius = 7

circle1 -= 3
circle1.show()  # Circle: Center at (0, 0), Radius = 4

circle4 = circle1 + 6
circle4.show()  # Circle: Center at (0, 0), Radius = 10

circle5 = circle4 - 4
circle5.show()  # Circle: Center at (0, 0), Radius = 6

# This will raise an error because radius cannot be negative
try:
    circle5 -= 10
except ValueError as e:
    print(e)  # Radius cannot be negative
