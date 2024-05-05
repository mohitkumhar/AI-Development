# 3. Create a class `Circle` with attribute `radius`. Add a method `calculate_area` that returns the area of the circle.


class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        
        return Circle.pi * self.radius * self.radius

circle1 = Circle(12)

result = circle1.calculate_area()

print(result)