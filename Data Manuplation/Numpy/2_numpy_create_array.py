# to create a numpy ndarray object 
# the array object in numpy is call ndarray

# array()
import numpy as np
x = np.array([1,2,3,4,5])
print(x)
print(type(x))

# we can also pass a list, tuple or any array like object with array(), and it will be converted to ndarray
import numpy as np
y = np.array((1,2,3,4,5))
print(x)
print(type(x))
# Dimensions in Array - a dimensions in arrays is one level of array depth(nested array)

# 0-D Arrays - scalars, are the elements in an array, each value in an array is a 0-D array.

# Now we will Create 0-D array with value 42
import numpy as np
x = np.array(42)
print(x)

# 1-D arrays - an array thar has 0-D arrays as its elements is called uni directional or 1-D
import numpy as np
x = np.array([1,2,3,4,5])
print(x)


# create a 2-D array containing 2 Arrays with certain values
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print(x)


# to create 3-D array with 2-D array
import numpy as np
x = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(x)

# ndim attribute: check how many dimensions the array have
import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# create an array with 5 dimensions and verify that it has 5 dimensions
import numpy as np
x = np.array([1,2,3,4,5], ndmin=5)
print(x)
print(f"Number of Dimensions: {x.ndim}")
