# Rayleigh Distribution - it is used in signal processing

# param - scale(standard deviaiton, how flat the distribution is .. {default - 1.0}), size(shape of the returned array)


# sample for the rayleigh distribution with scale of 2.0 with size of 2*3
from numpy import random
x = random.rayleigh(scale=2.0, size=(2,3))
print(x)

# visualisation of rayleigh distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(scale=2.0, size=1000), hist=False, label="RayLeigh")
sns.distplot(random.chisquare(df=2.0, size=1000), hist=False, label="ChiSquare")
plt.legend()
plt.show()


