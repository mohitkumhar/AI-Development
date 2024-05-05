# Operator Overloading lets you redefine how built-in operators like  "+" or "*" work with your custom classes (like your Vector class).

# Imagine you have special Vector objects. Normally, the "+" operator adds numbers. But with overloading, you can make it add the corresponding elements of two Vector objects!

# This makes your code more intuitive and readable. Like adding vectors with "+", instead of needing a special function.

# Remember: It's a powerful tool, but use it wisely to keep your code clear!



class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __sub__(self, x):
        return f"{self.i - x.i}i + {self.j - x.j}j + {self.k - x.k}k"
    
    def __add__(self, x):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    

v1 = Vector(11, 22, 33)
print(v1)

v2 = Vector(1, 2, 3)
print(v2)

print(v1 - v2)
print(v1 + v2)

