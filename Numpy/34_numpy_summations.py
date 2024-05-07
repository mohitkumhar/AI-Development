# summations: 
#            difference: addition is done between 2 arguments whereas summation happens over n elements


# adding the 2 array
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([1,2,3])
x = np.add(x1, x2)
print(x)    # [2 4 6]


# sum the values in 2 array
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([1,2,3])
x = np.sum([x1, x2])
print(x)    # 12


# summation over an axis: if you specify axis = 1, numpy will sum the number in each array
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([1,2,3])
x = np.sum([x1, x2], axis=1)
print(x)    # [6 6]


# cummulative sum - means partially adding the element in array
# example: [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10] {final answer}

# represent by cumsum()

import numpy as n
x1 = np.array([1,2,3,4])
x = np.cumsum(x1)
print(x)    # [ 1  3  6 10]


