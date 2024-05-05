# 7. Create a class `Animal` with a method `sound` that prints the sound the animal makes.


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound_type = sound
        
    def sound(self):
        print(f"{self.name} makes a {self.sound_type} sound")
    
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
        
class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        
        


dog1 = Dog("DoggerMan", "Bark")
dog1.sound()

cat1 = Cat("Tom", "Meowing")
cat1.sound()
        
        



