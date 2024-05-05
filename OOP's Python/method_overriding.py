# Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name, parameters, and return type as a method in its superclass, the subclass method overrides the superclass method, allowing for polymorphic behavior.


# Key Points about Method Overriding:

# Inheritance Relationship:

# Method overriding is applicable in the context of inheritance, where a subclass inherits from a superclass.

# The subclass can override (replace) a method defined in the superclass with its own implementation.

# Same Method Signature:

# Method overriding occurs when the subclass provides a method with the same name, parameters, and return type as a method in the superclass.

# Polymorphism:

# Method overriding enables polymorphism, where the same method name behaves differently depending on the object type.

# The method called depends on the actual object type (runtime object) rather than the reference type (compile-time type).


class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call make_sound method for Dog and Cat objects
print(dog.make_sound())  # Output: Woof! Woof!
print(cat.make_sound())  # Output: Meow!




# In this example:


# We have a base class Animal with a method make_sound that returns a generic animal sound.

# The Dog class and Cat class inherit from Animal and override the make_sound method with their specific implementations ("Woof! Woof!" for Dog and "Meow!" for Cat).

# When we create instances of Dog and Cat and call the make_sound method, each object invokes its own overridden version of the method, demonstrating polymorphic behavior.

# Rules for Method Overriding:

# The method in the subclass must have the same name, parameters, and return type as the method in the superclass to override it.

# The @override decorator is not required in Python, unlike some other languages, but it's a good practice to ensure you're actually overriding a method.

# Overridden methods can call the superclass method using super() to invoke the superclass's implementation in addition to providing specific behavior in the subclass.


# Calling Superclass Method from Subclass:
class Dog(Animal):
    def make_sound(self):
        # Call superclass method using super()
        return super().make_sound() + " and also barks loudly!"

# Create an instance of Dog
dog = Dog()
print(dog.make_sound())
# Output: Some generic animal sound and also barks loudly!


# We use super().make_sound() to call the make_sound method from the superclass (Animal) within the overridden make_sound method of Dog.

# By appending " and also barks loudly!" to the superclass's returned value, we provide additional behavior in the Dog class while still leveraging the superclass's functionality.


# Method overriding is a fundamental concept in object-oriented programming (OOP) that allows for code reusability, polymorphism, and customization of behavior in subclasses. It facilitates the implementation of the "is-a" relationship between classes and enables more flexible and maintainable code.