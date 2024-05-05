# Single inheritance in object-oriented programming (OOP), specifically Python, is when a class inherits properties and behaviors from one parent class. It's like a child getting traits from a single parent.

# Here's the breakdown:

# Parent class: This is the existing class with properties and methods you want to reuse. Think of it as the blueprint.
# Child class: This is the new class that inherits from the parent class. It gets all the parent's traits and can add its own unique ones. Imagine it as a specialization of the parent.



# Benefits:

# Code Reusability: You don't need to rewrite common code in the child class.
# Relationships: It helps model real-world relationships, like a Dog inheriting from Animal.
# Organized Code: It keeps your code modular and easier to understand.




class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a generic sound.")
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} (a {self.breed}) barks!")
        
    
animal = Animal("Generic Animal")
animal.make_sound()


dog = Dog("Buddy", "German")
dog.make_sound()
dog.bark()

