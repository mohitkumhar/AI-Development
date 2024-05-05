# 2. Create a class `Rectangle` with attributes `width` and `height`. Add a method `calculate_area` that returns the area of the rectangle.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

a1 = Rectangle(12, 12)

area = a1.calculate_area()

print(f"The Area of Rectangle is: {area} sq/m²")
