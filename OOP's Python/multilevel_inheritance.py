# Multilevel inheritance in Python is like having a chain of inheritance, where a class inherits from another class, which itself inherits from yet another class. Imagine a family tree: a child inherits from a parent, and the parent inherits from their own parent (grandparent).


# Multilevel inheritance in Python is like having a chain of inheritance, where a class inherits from another class, which itself inherits from yet another class. Imagine a family tree: a child inherits from a parent, and the parent inherits from their own parent (grandparent).



# Benefits:

# Code Reusability: You can reuse code from multiple levels of parent classes, building upon existing functionality.
# Modeling Real-World Relationships: It allows you to represent real-world scenarios where an object inherits traits from multiple levels of ancestors. For example, a Student class might inherit from a Person class (general attributes) and an Enrolled class (course-related attributes).


# Why We Use It (Cautiously):

# Clear Class Hierarchy: It's useful when there's a clear hierarchy of classes and inheritance makes sense.
# But Beware Complexity: Excessive multilevel inheritance can lead to complex code that's difficult to understand and maintain. Here's why:
# Increased Depth, Increased Challenges: Debugging and understanding code flow can become trickier as the inheritance chain grows longer.
# Method Resolution Order (MRO): Python has a specific order (MRO) to search for methods when there are multiple parent classes at higher levels. This can be confusing if methods with the same name exist across multiple ancestor classes.




class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
        
    def show_details(self):
        super().show_details()
        print(f"Breed: {self.breed}")
    
class Golden_Reteriver(Dog):
    def __init__(self, name, color):
        super().__init__(name, "Golden Reteriver")
        self.color = color
    
    def show_details(self):
        super().show_details()
        print(f"Color: {self.color}")
    
a1 = Golden_Reteriver("Tom", "Black")
a1.show_details()       

