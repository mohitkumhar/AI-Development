# 9. Create a class `Cat` that inherits from `Animal` and has an additional method `meow` which prints "Meow!"

class Animal:
    def __init__(self, name):
        self.name = name
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def meow(self):
        print("Meow!")

c1 = Cat("Kat")
c1.meow()
