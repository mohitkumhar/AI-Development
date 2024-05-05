# 8. Create a class `Dog` that inherits from `Animal` and has an additional method `bark` which prints "Woof!"


class Animal:
    def __init__(self, name):
        self.name = name
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def bark(self):
        print("Woof!")
    
dog1 = Dog("Buddy")
dog1.bark()

