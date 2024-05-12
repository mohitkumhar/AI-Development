# search array - you can search an array for a certain value and return the indexes that get the match. by using where

import numpy as np
x = np.array([1,2,3,4,5,4,4])

new_x = np.where(x == 4)
print(new_x)    # (array([3, 5, 6], dtype=int64),)


# indexes of even values
import numpy as np
x = np.array([1,2,3,4,5,6,7,8])

new_x = np.where(x % 2 == 0)
print(new_x)    # (array([1, 3, 5, 7], dtype=int64),)


# searchsorted() - perform binary search in array   

# find where value 7 will be inserted in array
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
new_x = np.searchsorted(x, 7)
print(new_x)   # 6


# to find the indexing from right side
import numpy as np
x = np.array([6,7,8,9])
new_x = np.searchsorted(x, 7, side='right')
print(new_x)  # 2


# how to search multiple value
import numpy as np
x = np.array([1,2,4,5,7])
new_x = np.searchsorted(x, [3,6,8])
print(new_x)  # [2 4 5]
