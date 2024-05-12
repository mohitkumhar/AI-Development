# 1-D array indexing is the same as accessing an array element start with 0 , second 1
import numpy as np
x = np.array([1,2,3,4])
print(x[1])

# to get the third and fourth elements from adding them 
import numpy as np
x = np.array([1,2,3,4])
print(x[2] + x[3])

# accessing the 2-D - it is like a rows and columns
import numpy as np
x = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f"5th element in the 2nd rows {x[1,4]}")



# accessing the 3-D - same as accessing 
import numpy as np
x = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(x[0,1,2])


