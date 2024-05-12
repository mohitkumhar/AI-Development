# finding LCM(lowest common multiple)

# to find the LCM of the Number:
import numpy as np
num1 = 4
num2 = 6
num = np.lcm(num1, num2)
print(num)   # 12


# reduce() - the reduce() method will use the ufunc, in below case the lcm() function on each element and it will reduce the array by 1 dimension

# to find lcm in array
import numpy as np
x = np.array([2,4,5,3])
ans = np.lcm.reduce(x)
print(ans)   # 60



# to find the LCM of all of an array where the array contains all integers from 1 to 10
import numpy as np
x1 = np.arange(1, 11)
x = np.lcm.reduce(x1)
print(x)    # 2520

