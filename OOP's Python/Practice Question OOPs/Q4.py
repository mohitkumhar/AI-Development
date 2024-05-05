# 4. Create a class `Student` with attributes `name` and `age`. Create a method `print_student_details` to print the details of the student.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_student_details(self):
        print(f"The Name of Student is: {self.name}")
        print(f"the Age is Student is : {self.age}")

student1 = Student("Mohit", 19)

student1.print_student_details()
        
