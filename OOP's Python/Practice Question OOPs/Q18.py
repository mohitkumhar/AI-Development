# 18. Create a class `Manager` that inherits from `Employee` and has an additional attribute `team_size`. Override the `calculate_bonus` method to return 15% of the salary.


class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_bonus(self):
        # Default Bonus Calculation for Employee
        return self.salary * 0.10

class Manager(Employee):
    def __init__(self, team_size, salary):
        self.team_size = team_size
        super().__init__(salary)
        
    def calculate_bonus(self):
        # Override the calculate_bonus Method for Manager (15% of Salary)
        return self.salary * 0.15

m1 = Manager(12, 100)

ans = m1.calculate_bonus()
print(ans)  # Output: 15
        


