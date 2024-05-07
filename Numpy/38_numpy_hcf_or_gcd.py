# finding GCD(Greatest Common Denominator), also known as HCF(Highest Common Factor)

# to find HCF of the 2 numbers
import numpy as np
num1 = 6
num2 = 9
num = np.gcd(num1, num2)
print(num)     # 3


# reduce() - the reduce() method will use the ufunc, in below case the gcd() function on each element and it will reduce the array by 1 dimension

# finding the gcd in array
import numpy as np
x1 = np.array([20,8,32,16,36])
x = np.gcd.reduce(x1)
print(x)     # 4


