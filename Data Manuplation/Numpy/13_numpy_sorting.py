# sort() - used to sort a specified array

import numpy as np
x = np.array([3,2,0,1])
print(np.sort(x))  # this method is like the copy (original array is unchanged)


# sort the array alphabetically
import numpy as np
x = np.array(['cherry', 'banana', 'apple'])
print(np.sort(x))


# sort the boolean array
import numpy as np
x = np.array([True, False, True])
print(np.sort(x))


# sorting the 2-D array
import numpy as np
x = np.array([[4,2,6], [5,7,1]])
print(np.sort(x))
