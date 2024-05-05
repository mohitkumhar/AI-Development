# 1. Create a Python class named `Person` with attributes `name` and `age`. Initialize an object with these attributes and print them.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"The Name of Person is: {self.name}")
        print(f"The Age of a Person is: {self.age}")
    
person1 = Person("Mohit", 19)
person1.show_info()