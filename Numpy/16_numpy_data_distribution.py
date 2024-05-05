# data distribution is a list of all possible value and how often each value occure
# such lists are important when working with statistics and data science

# random distribution: probability function 

# now we will generate 1-D with 100 values where each value has to be 3,5,7,9

# the probability for the value 3 is set to be 0.1
# the probability for the value 5 is set to be 0.3
# the probability for the value 7 is set to be 0.6
# the probability for the value 9 is set to be 0
# The sum of all probability numbers should be 1

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=10)
print(x)


# now we will 2-D with 3 rows containing 5 values
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

