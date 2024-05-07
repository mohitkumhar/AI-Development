# to create your own ufunc, you have to define a function, like you do in normal function in python, then you add it to the numpy function with frompyfunc() method.

# arguments of frompyfunc(): function, inputs, outputs


# create your own ufunc for addition:
import numpy as np
def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))



# chekcing if this function is ufunc or not
import numpy as np
print(type(np.add))

# concatenate()
import numpy as np
print(type(np.concatenate))


# what if ufunc does not exist:
import numpy as np
'''print(type(np.mohit))'''

# use an if statement to check if the function is a ufunc or not
import numpy as np
if type(np.add) == np.ufunc:
    print("Yes, This Function is ufunc")
else:
    print("No, this Function is not an ufunc")
