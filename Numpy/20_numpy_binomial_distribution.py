# binomial dist - discrete dist- binary output

# param - n(number of trials), p(probability), size(shape-returned array)

# given 10 trial for a coin which will generate 10 data points:
from numpy import random
x = random.binomial(n=10, p=0.7, size=10)
print(x)

# visualisation of binomial dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=False, kde=True)
plt.show()


# Diff between normal and binomial - normal(continues) and binomial(discrete)

# use 500 data point for binomial and 100 data point for normal distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, kde=True, label="Normal")
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, kde=True, label="Binomial")
plt.legend()
plt.show()