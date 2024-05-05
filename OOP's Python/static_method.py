class Math:
    def __init__(self, num1):
        self._num1 = num1
    
    def sum1(self, num2):
        self._num1 = num2 + self._num1
    
    # @staticmethod
    def add(self):
        print(f"The Result Will Be: {self._num1}")

a1 = Math(4)
answer = a1.sum1(2)
a1.add()
