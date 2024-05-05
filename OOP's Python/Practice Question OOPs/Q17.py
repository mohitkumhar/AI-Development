# 17. Create a class `Square` that inherits from `Rectangle` and has a method `calculate_perimeter` to calculate the perimeter.


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        

    
r1 = Rectangle(12, 10)
rect_peri = r1.calculate_perimeter()
print(rect_peri)

sq1 = Square(10)
sq_peri = sq1.calculate_perimeter()
print(sq_peri)

