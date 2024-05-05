# Iterating Array - means going through the elements one by one or step by step like for-loop

# Iterate the element of 1-D
import numpy as np
x = np.array([1,2,3])
for i in x:
    print(i)

# Iterate the element of 2-D
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
for i in x:
    for j in i:
        print(j)

# Iterate the element of 3-D
import numpy as np
x = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for i in x:
    for j in i:
        for k in j:
            print(k)


# Iterating arrays using nditer() function
# Now we will Iterate on each scalar element

import numpy as np
x = np.array([[[1,2], [3,4], [5,6], [7,8]]])
for i in np.nditer(x):
    print(i)


# Now we will iterate with different step sizes

import numpy as np
x = np.array([[1,2,3,4], [5,6,7,8]])
for i in np.nditer(x[:, ::2]):
    print(i)

