# slicing array - slicing in python taking elements f
# one given index to another index
# [start:end] or [start:end:steps]


# to slice an element from 1 to 5:
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[1:5])


# to slice from index 4 to end value 
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[4:])


# to slice from the begining to index 4
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[:4])


# Negative Slicing - index 3 to end
import numpy as np
x = np.array([1,2,3,4,5,6,7])
print(x[-3:-1])


# Step - we can use step value to determine the step of the slicing 

# return every oother value from index 1 to 5
import numpy as np
x = np.array([1,2,3,4,5,6,7])
print(x[1:5:2])


# to return every other number from the entire array
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[::2])

# slicing 2-D array: print 7,8,9
import numpy as np
x= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(x[1,1:4])


# another example
import numpy as np
x = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(x[0:2, 2])


# another example tough 2-D - print from both, index 1:4
import numpy as np
x = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(x[0:2, 1:4])
