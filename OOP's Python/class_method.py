# In Python, class methods are special methods bound to the class itself rather than an instance of the class. They are defined using the @classmethod decorator and have access to the class itself (via cls) rather than individual instances (via self).

# Here are the key characteristics and usage of class methods in Python:

# Characteristics of Class Methods:

# Class methods are defined using the @classmethod decorator.

# They are bound to the class itself and can be called on the class (e.g., ClassName.method()).

# Class methods take the class itself (cls) as the first parameter, conventionally named cls.

# They can access and modify class-level data (class variables) and perform operations that are not specific to any particular instance.

# Use Cases for Class Methods:

# Alternative Constructors: Class methods are often used as alternative constructors to provide multiple ways of creating instances of a class.

# Accessing Class Variables: They can access and modify class variables, which are shared among all instances of the class.

# Performing Class-level Operations: Class methods can perform operations that involve the class itself, such as updating class-level data or performing initialization tasks.



class Employee:
    company = "Apple"
    def show(self):
        print(f"The Name is {self.name} and comapny is {self.company}")
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        

e1 = Employee()
e1.name = "Mohit"
e1.show()
e1.change_company("Google")
e1.show()
print(Employee.company)


