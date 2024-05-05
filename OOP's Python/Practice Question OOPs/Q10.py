# 10. Create a class `Employee` with attributes `name`, `salary`, and `role`. Create a method `calculate_bonus` that returns 10% of the salary.


class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def calculate_bonus(self):
        bonus = self.salary * 0.1
        return bonus

e1 = Employee("Mohit", 1000, "AI Developer")
result = e1.calculate_bonus()
print(result)
