# 16. Create a class `Vehicle` with attributes `speed` and `mileage`. Add a method `calculate_travel_time` that calculates the time taken to travel a given distance.


class Vehicle:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage
    
    def calculate_travel_time(self, distance):
        return distance / self.speed

v1 = Vehicle(100, 150)

time = v1.calculate_travel_time(100)
print(time)


