# tigonometric function - numpy provides the ufuncs line sin(), cos() and tan() that takes values on radians and produce the corresponding sin, cos and tan values.


# to find the sin value of pi/2
import numpy as np
x = np.sin(np.pi/2)
print(x)     # 1.0


# to find the sin values of an array
import numpy as np
x1 = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

x = np.sin(x1)
print(x)     # [0.   0.5        0.70710678   0.8660254  1. ]


# convert degree into radian - by default all of the trigonometric functions takes radians as a parameter   (we can change it)

# Note: radians values are pi/180° degree value


# to convert all the array values from degree to radian 
import numpy as np
x1 = np.array([90, 180, 270, 360])
x = np.deg2rad(x1)
print(x)     # [1.57079633 3.14159265 4.71238898 6.28318531]   


# to convert all the array values from radian to degree
import numpy as np
x1 = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(x1)
print(x)     # [ 0. 30. 45. 60. 90.]



# we can also find angles - arcsin(), arccos() and arctan() that takes values in radians and produce the corresponding sin, cos and tan values

# in other word arcsin() is used to find the inverse of sin

# to find the angle of 1.0
import numpy as np
x = np.arcsin(1.0)
print(x)     # 1.5707963267948966

# arcsin() - by using array
import numpy as np
x1 = np.array([1.0, 0.5, -1.0, -0.5])
x = np.arcsin(x1)
print(x)     # [ 1.57079633  0.52359878 -1.57079633 -0.52359878]


# to findthe hypotenous using the pythagoras theoram in numpy

# hypot() - this function takes values in radians and produce the corresponding sin, cos and tan values

# to find the hypot for 3 base and 4 perpendicular
import numpy as np
base = 3
per = 4
x = np.hypot(base, per)
print(x)





