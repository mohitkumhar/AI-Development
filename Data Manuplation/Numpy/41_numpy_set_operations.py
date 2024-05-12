# set - it is the collection of unique elements


# for creating the set we use numpy's unique() method to find the unique elements from any array:

# to convert the array with repeated elements to a set
import numpy as np
x1 = np.array([1,1,1,2,3,4,5,5,6,7])
x = np.unique(x1)
print(x)     # [1 2 3 4 5 6 7]


# to find the unique values of 2 array, we will use union1d() method
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([3,4,5,6])
x = np.union1d(x1, x2)
print(x)     # [1 2 3 4 5 6]


# to find the only values that are present in both array we will use intersert1d() method
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([3,4,5,6])
x = np.intersect1d(x1, x2, assume_unique=True)     # assume_unique=True (it increases the computation speed)
print(x)     # [3 4]


# to find the only values that are in 1st set and NOT present in the 2nd set: use setdiff1d()
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([3,4,5,6])
x = np.setdiff1d(x1, x2, assume_unique=True)
print(x)    # [1 2]


# to find the only values that are NOT present in BOTH the sets, use setxor1d() method or non-common elements
import numpy as np
x1 = np.array([1,2,3,4])
x2 = np.array([3,4,5,6])
x = np.setxor1d(x1, x2, assume_unique=True)
print(x)    # [1 2 5 6]





