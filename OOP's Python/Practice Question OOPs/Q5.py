# 5. Create a class `BankAccount` with attributes `balance` and methods `deposit` and `withdraw` to add or subtract money from the balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return None
        
        else:
            self.balance = self.balance - withdraw
            return self.balance

acc1 = BankAccount(1000)

total_balance = acc1.deposit(100)

print(f"The Total Balance After Deposit is: {total_balance}")

balance_after_withdraw = acc1.withdraw(600)
if balance_after_withdraw:
    print(f"The Total Balance After WithDraw is: {balance_after_withdraw}")


    
        