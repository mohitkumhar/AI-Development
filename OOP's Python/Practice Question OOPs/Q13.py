# 13. Create a class `Bank` with attributes `name` and `branches`. Add a method `add_branch` to add a new branch to the bank.

class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []
        
    def add_branch(self, new_branch):
        self.branches.append(new_branch)
    
b1 = Bank("Mohit")
b1.add_branch("Udaipur")
b1.add_branch("Jaipur")

print(b1.branches)


