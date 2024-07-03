"""
Create a base class Shape to draw flat shapes.

Define the following methods:

Show() — print info about a shape;
Save() — save a shape to a file;
Load() — read a shape from a file.
Define the derived classes:

Square — a square defined by the coordinates of the upper left corner and the side length;
Rectangle — a rectangle with the specified coordinates of the upper left corner and dimensions;
Circle — a circle with the specified coordinates of the center and radius;
Ellipse — an ellipse with the specified coordinates of the top corner of a circumscribed rectangle with its sides parallel to the coordinate axes, and the dimensions of this rectangle.
Create a list of shapes, save the shapes to a file, load into another list, and display information about each shape.

Translate:
Vytvořte základní třídu Shape pro kreslení plochých tvarů.

Definujte následující metody:

Show() — vypiš informace o tvaru;
Save() — ulož tvar do souboru;
Load() — načti tvar ze souboru.
Definujte odvozené třídy:

Square — čtverec definovaný souřadnicemi horního levého rohu a délkou strany;
Rectangle — obdélník se zadanými souřadnicemi horního levého rohu a rozměry;
Circle — kruh se zadanými souřadnicemi středu a poloměrem;
Ellipse — elipsa se zadanými souřadnicemi horního rohu opsaného obdélníku se stranami rovnoběžnými s osami souřadnic a rozměry tohoto obdélníku.
Vytvořte seznam tvarů, uložte tvary do souboru, načtěte je do dalšího seznamu a zobrazte informace o každém tvaru.

"""


class Shape:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.serialize())

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            data = f.read()
        return Shape.deserialize(data)

    def serialize(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def deserialize(data):
        lines = data.split('\n')
        shape_type = lines[0]
        if shape_type == "Square":
            return Square.deserialize(data)
        elif shape_type == "Rectangle":
            return Rectangle.deserialize(data)
        elif shape_type == "Circle":
            return Circle.deserialize(data)
        elif shape_type == "Ellipse":
            return Ellipse.deserialize(data)
        else:
            raise ValueError("Unknown shape type")

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square: Top-left corner at ({self.x}, {self.y}), Side length = {self.side_length}")

    def serialize(self):
        return f"Square\n{self.x}\n{self.y}\n{self.side_length}"

    @staticmethod
    def deserialize(data):
        lines = data.split('\n')
        return Square(int(lines[1]), int(lines[2]), int(lines[3]))

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle: Top-left corner at ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}")

    def serialize(self):
        return f"Rectangle\n{self.x}\n{self.y}\n{self.width}\n{self.height}"

    @staticmethod
    def deserialize(data):
        lines = data.split('\n')
        return Rectangle(int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4]))

class Circle(Shape):
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Circle: Center at ({self.cx}, {self.cy}), Radius = {self.radius}")

    def serialize(self):
        return f"Circle\n{self.cx}\n{self.cy}\n{self.radius}"

    @staticmethod
    def deserialize(data):
        lines = data.split('\n')
        return Circle(int(lines[1]), int(lines[2]), int(lines[3]))

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Ellipse: Top-left corner of bounding rectangle at ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}")

    def serialize(self):
        return f"Ellipse\n{self.x}\n{self.y}\n{self.width}\n{self.height}"

    @staticmethod
    def deserialize(data):
        lines = data.split('\n')
        return Ellipse(int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4]))

# Create a list of shapes
shapes = [
    Square(10, 10, 5),
    Rectangle(20, 20, 10, 5),
    Circle(15, 15, 7),
    Ellipse(5, 5, 20, 10)
]

# Save each shape to a file
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.txt')

# Load shapes into a new list
loaded_shapes = []
for i in range(len(shapes)):
    shape = Shape.load(f'shape_{i}.txt')
    loaded_shapes.append(shape)

# Show information about each loaded shape
for shape in loaded_shapes:
    shape.show()
