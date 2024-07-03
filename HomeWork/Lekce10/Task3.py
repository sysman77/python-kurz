class Shape:
    def show(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(self.__class__.__name__ + "\n")
            for key, value in self.__dict__.items():
                file.write(f"{key}:{value}\n")
            file.write("\n")
    
    @classmethod
    def load(cls, filename):
        shapes = []
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line:
                shape_type = line
                shape_attrs = {}
                i += 1
                while i < len(lines) and lines[i].strip():
                    key, value = lines[i].strip().split(":")
                    shape_attrs[key] = float(value) if '.' in value else int(value)
                    i += 1
                shape_class = globals()[shape_type]
                shape = shape_class.__new__(shape_class)
                shape.__dict__.update(shape_attrs)
                shapes.append(shape)
            i += 1
        return shapes

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length
    
    def show(self):
        print(f"Čtverec: Levý horní roh ({self.x}, {self.y}), délka strany {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        print(f"Obdélník: Levý horní roh ({self.x}, {self.y}), šířka {self.width}, výška {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def show(self):
        print(f"Kruh: střed ({self.x}, {self.y}), poloměr {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        print(f"Elipsa: Vymezení horního levého rohu ({self.x}, {self.y}), šířka {self.width}, výška {self.height}")

# Vytvoření seznamu tvarů
shapes = [
    Square(1, 2, 5),
    Rectangle(2, 3, 4, 6),
    Circle(5, 5, 3),
    Ellipse(0, 0, 7, 4)
]

# Uložení tvarů do souboru
filename = "tvary.txt"
for shape in shapes:
    shape.save(filename)

# Načtení tvarů do nového seznamu
loaded_shapes = Shape.load(filename)

# Zobrazení informací o načtených tvarech
for shape in loaded_shapes:
    shape.show()
