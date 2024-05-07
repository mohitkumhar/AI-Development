# arithmetic operators: +, -, *, /

# by using ufunc additional arguments like, where, dtype and out 

# add()
import numpy as np
x1 = np.array([10,11,12,13,14,15])
x2 = np.array([20,21,22,23,24,25])
x = np.add(x1, x2)
print(x)    # [30 32 34 36 38 40]


# subtract()
import numpy as np
x1 = np.array([10,11,12,13,14,15])
x2 = np.array([20,21,22,23,24,25])
x = np.subtract(x1, x2)
print(x)    # [-10 -10 -10 -10 -10 -10]


# multiply()
import numpy as np
x1 = np.array([10,11,12,13,14,15])
x2 = np.array([20,21,22,23,24,25])
x = np.multiply(x1, x2)
print(x)    # [200 231 264 299 336 375]


# divide()
import numpy as np
x1 = np.array([10,11,12,13,14,15])
x2 = np.array([20,21,22,23,24,25])
x = np.divide(x1, x2)
print(x)    # [0.5        0.52380952 0.54545455 0.56521739 0.58333333 0.6       ]


# power() - this function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array
import numpy as np
x1 = np.array([10,20,30,40,50,60])
x2 = np.array([3,5,6,8,2,13])
x = np.power(x1, x2)
print(x)    # [      1000    3200000  729000000 -520093696       2500 1006632960]


# reminder - mod() or reminder() functions return the reminder of the 1st array corresponding to the 2nd array, and result in the new array

# mod()
import numpy as np
x1 = np.array([10,20,30,40,50,60])
x2 = np.array([3,7,9,8,2,33])
x = np.mod(x1, x2)
print(x)    # [ 1  6  3  0  0 27]

# remainder()
import numpy as np
x1 = np.array([10,20,30,40,50,60])
x2 = np.array([3,7,9,8,2,33])
x = np.remainder(x1, x2)
print(x)    # [ 1  6  3  0  0 27]


# quotient and mod/remainder
# divmod() - function return both the quotient and mod/remainder
import numpy as np
x1 = np.array([10,20,30,40,50,60])
x2 = np.array([3,7,9,8,2,33])
x = np.divmod(x1, x2)
print(x)    # (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))


# absolute() / abs() - do the same operation but here we should use absolute() to aboid confusion with python inbuilt finction math.abs()

import numpy as np
x = np.array([-1,-2,-3,-4,-5,6])
new_x = np.absolute(x)
print(new_x)    # [1 2 3 4 5 6]
