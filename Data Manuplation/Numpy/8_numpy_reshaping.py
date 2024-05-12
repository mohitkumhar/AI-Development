# Reshaping - means changing the shape of an array ,  like adding or removing the elements

# reshaping from 1-D to 2-D

import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

new_x = x.reshape(4, 3)
print(new_x)


# reshaping from 1-D to 3-D

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_x = x.reshape(2, 3, 2)
print(new_x)