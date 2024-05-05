# poisson Dist - it estimates how many time an event can happen

# param - lam(number of occurance or rate), size

# generate a random 1*10 dist for the occurance 2

from numpy import random
x = random.poisson(lam=2, size=10)
print(x)

# visualisation of poisson dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))
# plt.show()


# presenting both the polts in same figure normal and poisson dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=10, size=1000), hist=False, label="Normal", kde=True)
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="Poisson", kde=True)
plt.legend()
plt.show()

# n(number of times (binomial)) * p(probability) == lam (in poission)