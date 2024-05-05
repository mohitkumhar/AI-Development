
# shape of the array - the shape of an array is the number of element in each dimensions

# now we will try to get the shape of any array

import numpy as np
x = np.array([[1,2,3,4], [5,6,7,8]])
print(x.shape)    # (2, 4)

# (2, 4) here, 2 is the dimension and 4 is the number of elements


# now we will create a 5-D array using ndmin:
import numpy as np
x = np.array([1,2,3,4, 5], ndmin=5)
print(x)
print(x.shape)
