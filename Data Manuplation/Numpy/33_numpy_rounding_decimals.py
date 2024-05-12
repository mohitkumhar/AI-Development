# rounding decimals - there are 5 ways of rounding off the decimals in numpy: truncation, fix, rounding, floor, ceil


# truncation - trunc() / fix()

# these command remove the decimals and return the float number closest to zero


# trunc()
import numpy as np
x = np.trunc([-3.1666, 3.6667])
print(x)    # [-3.  3.]

# fix()
import numpy as np
x = np.fix([-3.1666, 3.6667])
print(x)    # [-3.  3.]

    
# rounding - the around() function increments preceding digit or dicimal by nearest to 1: if n>5 = 1 or n<5 = 0
import numpy as np
x = np.around(3.1666, 2)
print(x)    # 3.17


# floor() - round off decimals to the lower integer
import numpy as np
x = np.floor([-3.1666, 3.6667])
print(x)    # [-4.  3.]


# ceil() - round off decimals to the upper integer
import numpy as np
x = np.ceil([-3.1666, 3.6667])
print(x)    # [-3.  4.]