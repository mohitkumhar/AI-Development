# Random real meaning - something that cannot be predicted logically



# generate random number from 0 to 100
from numpy import random
x = random.randint(100)
print(x)



# rand() - to generate float
from numpy import random
x = random.rand()
print(x)


# to generate random array 1-D form 0-100
from numpy import random
x = random.randint(100, size=(5))
print(x)


# generate a 2-D array with 3 rows, each row containing 5 random int from 0 to 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)


# to generate random 1-D float array containing 5 random float
from numpy import random
x = random.rand(5)
print(x)


# to generate random 2-D float array with 3 rows containing 5 random float
from numpy import random
x = random.rand(3, 5)
print(x)


# choice() - to generate random numbers from an array or list
from numpy import random
x = random.choice([1,2,3,4,5,6])
print(x)

# to generate random numbers from 2-D array
from numpy import random
x = random.choice([1,2,3,4,5,6], size=(3, 5))
print(x)
'''
Output 
    [[3 5 5 6 4]
    [4 2 4 2 3]
    [3 5 4 5 1]]
'''

