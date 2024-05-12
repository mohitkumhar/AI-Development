# joining the numpy array - here for this we will pass concatenate()


# 1-D array

import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x = np.concatenate((x1, x2))
print(x)

# Joining of 2-D array along with rows(axis = 1) or column(axis = 0 { Default })

import numpy as np
x1 = np.array([[1,2], [3,4]])
x2 = np.array([[5,6], [7,8]])
x = np.concatenate((x1, x2), axis=1)
print(x)


# Stack function- Concatenate array with respect to index
# Joining array using stack function
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x = np.stack((x1, x2), axis=1)
print(x)


# hstack() - stacking along with rows
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x = np.hstack((x1, x2))
print(x)


# vstack() - stacking along with column
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x = np.vstack((x1, x2))
print(x)


# dstack() - stacking along with depth or height
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
x = np.dstack((x1, x2))
print()
print()
print(x)
