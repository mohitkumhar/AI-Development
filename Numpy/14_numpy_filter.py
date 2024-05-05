# Getting some elements out of an existing array and creating a new array is called filtering

# a boolean index list is a list of boolean correspoinding to indexes in the array. (True and False)

 

# create an array from the element on index 0 and 2
import numpy as np
x1 = np.array([41,42,43,44])
x2 = [True, False, True, False]
x = x1[x2]
print(x)


# now we will create a filter array that will return only values higher than 42
import numpy as np
x = np.array([41,42,43,44])
filter_x = []
for i in x:
    if i > 42:
        filter_x.append(True)
    else:
        filter_x.append(False)

final_x = x[filter_x]
print(final_x)


# create a filter array that will return only even elements from the original array.

import numpy as np
x1 = np.array([1,2,3,4,5,6,7,8,9,10])
filter_x1 = []

for i in x1:
    if (i % 2 == 0):
        filter_x1.append(True)
    else:
        filter_x1.append(False)
    
x = x1[filter_x1]
print(filter_x1)
print(x)


# create filter directly from array (alternative way)
import numpy as np
x1 = np.array([41,42,43,44])
filter_x = x1 > 41
x = x1[filter_x]
print(filter_x)
print(x)
