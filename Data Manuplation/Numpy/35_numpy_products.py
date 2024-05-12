# products: use prod() function
# prod() - [1,2,3,4] = (1*2*3*4) = 24

# to find the product of the element of the below array
import numpy as np
x1 = np.array([1,2,3,4])    # 1*2*3*4
x = np.prod(x1)
print(x)    # 24


# to find the product of elements in 2 different array:
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([5,6,7,8])
x = np.prod([x1, x2])   # (1*2*3*4)*(5*6*7*8)
print(x)    # 40320


# product over an axis
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([5,6,7,8])
x = np.prod([x1, x2], axis=1)   # [(1*2*3*4) (5*6*7*8)]
print(x)    # [  24 1680]


# commutative product: cumprod()
# example the partial product of [1,2,3,4] is [1  1*2  1*2*3  1*2*3*4] = [1 2 6 24]

# cumprod()
import numpy as np
x1 = np.array([1,2,3,4])
x = np.cumprod(x1)   # [1  1*2  1*2*3  1*2*3*4]
print(x)    # [ 1  2  6 24]





