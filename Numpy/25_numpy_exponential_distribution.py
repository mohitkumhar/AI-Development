# Exponential Distribution - it is used for describing the time till next evenet that is like failure or success

# param - scale(inverse of rate(check lam in poisson distribution)), size


# draw a sample for a exponential distribution with 2.0 scale and 2*3 size

from numpy import random
x = random.exponential(scale=2, size=(2,3))
print(x)


# visualisation of exponential distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

