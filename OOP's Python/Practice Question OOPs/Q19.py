# 19. Create a class `BankAccount` with attributes `balance` and `interest_rate`. Add a method `calculate_interest` that returns the interest earned based on the balance and interest rate.


class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        # Assuming the time is 1 year
        return (self.balance * self.interest_rate) / 100
    
acc1 = BankAccount(1000, 10)
total_interest = acc1.calculate_interest()
print(total_interest)
        

