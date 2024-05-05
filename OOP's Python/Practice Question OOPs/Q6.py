# 6. Create a class `Car` with attributes `make`, `model`, and `year`. Create a method `get_info` to print the details of the car.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        print(f"The car is a {self.year} {self.make} {self.model}")
        
car1 = Car("Ford", "Fusion", 2019)

car1.get_info()



