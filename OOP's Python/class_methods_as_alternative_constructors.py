# In Python, class methods can be used as alternative constructors to provide different ways of creating instances of a class. This means you can use a class method to create objects using different input formats or parameters, providing more flexibility when initializing objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def create_from_string(cls, data_string):
        # Parse the data_string to extract name and age
        # name, age = data_string.split('-')
        return cls(data_string.split('-')[0], data_string.split('-')[1])

# Using the class method to create Person objects
person1 = Person("Alice", 30)
person2 = Person.create_from_string("Bob-25")

# Display information about each person
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25


