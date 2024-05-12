# Data type in Numpy

# i for integer
# b for boolean
# u for unsigned
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V memory


# checking The Data Type of numpy array - integer

import numpy as np
x = np.array([1,2,3,4])
print(x.dtype)


# checking The Data Type of numpy array - string

import numpy as np
x = np.array(['apple', 'banana'])
print(x.dtype)


# creating array with definite datatype

import numpy as np
x = np.array([1,2,3,4], dtype='S')  # S for string
print(x)
print("this is string: ",x.dtype)


# now we will create an array with a datatype of 4 byte int

import numpy as np
x = np.array([1,2,3,4], dtype='i4')  # i for integer
print(x)
print("Check", x.dtype)


# This casting is not possible Error will be raise

import numpy as np
# x = np.array(['apple', 'banana'], dtype='i')   # Leads to Error
# print(x)
# print(x.dtype)


# Converting datatype in existing array - astype()
# ( astype() function in numpy is used to convert the data type of elements in a numpy array to a specified data type. It creates a new array with the desired data type )

import numpy as np
x = np.array([1.1, 2.1, 3.1, 4.1])
new_x = x.astype('i')
print("This is astype: ", new_x)
print("This is astype: ", new_x.dtype)


# Converting datatype form integer to boolean

import numpy as np
x = np.array([1,0,1,1])
new_x = x.astype(bool)
print(new_x)
print(new_x.dtype)
