# Permutation refers to an arrangements of an elements like [3,2,1] is permutation of [1,2,3] and vice versa

# the numpy random module provides 2 methods: shuffle() and permutation()

# shuffle() method state changes to the original array


# to randomly shuffle elements for the array:
from numpy import random
import numpy as np

x = np.array([1,2,3,4,5])
random.shuffle(x)
print(x)


# to generate a permutation of elements for the array:

# the permutation() methods leaves the original array unchanged
from numpy import random
import numpy as np
x = np.array([1,2,3,4,5])
print(random.permutation(x))



    