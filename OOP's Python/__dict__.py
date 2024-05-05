# the __dict__ method is not a method but a special attribute in Python that provides a dictionary containing the namespace of an object or class. This dictionary holds the attributes (variables) defined for the object or class.


# When you access __dict__ on an instance (obj.__dict__), it returns a dictionary containing the instance variables (attributes) defined for that particular object.

class Person:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

# Create an instance of Person
person = Person("Alice", 30, 8)

# Access the __dict__ attribute of the instance
print(person.__dict__)
# Output: {'name': 'Alice', 'age': 30, 'roll': 8}
