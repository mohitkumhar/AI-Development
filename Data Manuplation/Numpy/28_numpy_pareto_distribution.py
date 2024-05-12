# Pareto Distribution - it is 80:20 ratio. (20% factors Cause 80% outcome or result )

# param - a(shape), size


# sample of pareto distribution with shape 2 and size 2*3
from numpy import random
x = random.pareto(a=2, size=(2,3))
print(x)


# visualisation of pareto distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000), hist=False)
plt.show()


