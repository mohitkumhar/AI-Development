# uniform dist - it is only made for probability(p)
# param - a(lower bound 0.0), b(upper bound 1.0), size

from numpy import random
x = random.uniform(size=(2,3))
print(x)


# visualisation of uniform distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
