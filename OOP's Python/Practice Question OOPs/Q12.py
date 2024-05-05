# 12. Create a class `Point` with attributes `x` and `y`. Add a method `distance_to_origin` that calculates the distance from the point to the origin (0,0).

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        distance = math.sqrt(self.x ** 2 + self.y ** 2)
        
        return distance

pt1 = Point(1, 4)

total_distance = pt1.distance_to_origin()

print(total_distance)

