# 11. Create a class `Triangle` with attributes `side1`, `side2`, and `side3`. Add a method `is_equilateral` to check if the triangle is equilateral.

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def is_equilateral(self):
        return self.side1 == self.side2 and self.side2 == self.side3

t1 = Triangle(12, 12, 12)

answer = t1.is_equilateral()
print(answer)
