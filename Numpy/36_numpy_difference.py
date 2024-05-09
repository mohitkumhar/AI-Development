# difference: use diff() function for finding the difference

# example: [1,2,3,4] - the deiscreate difference of this would be [2-1, 3-2, 4-3] = [1,1,1] by using diff()
import numpy as np
x1 = np.array([10,15,25,5])
x = np.diff(x1)     # [15-10, 25-15, 5-25]
print(x)     # [5 10 -20]
