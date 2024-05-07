# tigonometric function - numpy provides the ufuncs line sinh(), cosh() and tanh() that takes values on radians and produce the corresponding sin, cos and tan values.

# to find the value of sinh of pi/2
import numpy as np
x = np.sinh(np.pi/2)
print(x)


# to find the values in array
import numpy as np
x1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sinh(x1)     # [2.3012989  1.24936705 0.86867096 0.670484]   
print(x)


# to find cosh value in array
import numpy as np
x1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(x1)     # [2.50917848 1.60028686 1.32460909 1.20397209]
print(x)
# to find cosh value in array
import numpy as np
x1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(x1)     # [2.50917848 1.60028686 1.32460909 1.20397209]
print(x)


# to find cosh value in array
import numpy as np
x1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.tanh(x1)     # [0.91715234 0.78071444 0.6557942  0.55689331]
print(x)


# we can also find angles - arcsinh(), arccosh() and arctanh() that takes va
# lues in radians and produce the 
# corresponding sin, cos and tan values

# to find the angle of 1.0
import numpy as np
x = np.arcsinh(1.0)
print(x)     # 0.881373587019543

# arctanh() - by using array
import numpy as np
x1 = np.array([0.1, 0.2, 0.5])
x = np.arctanh(x1)
print(x)     # [0.10033535 0.20273255 0.54930614]




