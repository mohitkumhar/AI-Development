# 15. Create a class `Shape` with an abstract method `area`. Create subclasses `Rectangle` and `Circle` that implement this method.


from abc import abstractmethod

class Shape:
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

r1 = Rectangle(3, 4)
rect_area = r1.area()
print(rect_area)

c1 = Circle(2)
circle_area = c1.area()
print(circle_area)
    


