# In Python, instance variables and class variables are both types of variables used within classes, but they serve different purposes and have different scopes.

# Instance Variable:
# An instance variable is a variable that is tied to a specific instance of a class.

# Each instance of the class (i.e., each object created from the class) can have its own separate copy of the instance variables.

# Instance variables are defined inside methods with self as a prefix within the class.

# They are accessed using the instance (self) within methods of the class or from outside the class using the instance object.

# Instance variables hold data unique to each instance of the class.


# Class Variable:

# A class variable is a variable that belongs to the class itself rather than any specific instance.

# There is only one copy of a class variable shared among all instances of the class.

# Class variables are defined directly within the class but outside of any instance methods, typically at the beginning of the class.

# They are accessed using the class name (ClassName) or through an instance of the class (self), but any modifications to the class variable affect all instances of the class.


class Car:
    total_cars = 0  # Class variable to track total number of cars
    
    def __init__(self, make, model, year):
        self.make = make      # Instance variable for car make
        self.model = model    # Instance variable for car model
        self.year = year      # Instance variable for car year
        
        Car.total_cars += 1   # Increment total cars count when a new instance is created
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")
    
    @classmethod
    def display_total_cars(cls):
        print(f"Total Cars Created: {cls.total_cars}")

# Creating instances of Car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Display information about each car
car1.display_info()  # Output: Car: 2020 Toyota Corolla
car2.display_info()  # Output: Car: 2018 Honda Civic

# Display total number of cars created
Car.display_total_cars()  # Output: Total Cars Created: 2


# In this example, we'll create a Car class to represent different cars. Each car will have instance variables like make, model, and year, which are specific to each car instance. Additionally, we'll use a class variable total_cars to keep track of the total number of cars created.

