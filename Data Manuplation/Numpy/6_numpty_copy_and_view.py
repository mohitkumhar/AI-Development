# difference between numpy array copy and view

# copy : This means it creates a completely independent copy of the array, including its data and dimensions. Modifying the copy will not affect the original array

import numpy as np
x = np.array([1,2,3,4,5])
new_x = x.copy()
print(x)
print(new_x)
x[0] = 12
print(x)
print(new_x)


# view : The view is dependent on original array and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

import numpy as np
x = np.array([1,2,3,4,5])
new_x = x.view()
print(x)
print(new_x)
x[0] = 33
print(x)
print(new_x)