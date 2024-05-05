# logistic destribution - describe growth it is basically imp in regression and neural network

# param - loc(mean {default value = 0}), scale(standard deviation {default value = 1}), size


# draw 2 * 2 samples of logistic with mean at 1 and stddev(standard deviation) 2
from numpy import random
x = (random.logistic(loc=1, scale=2, size=10))
print(x)


# visualisation of logistic distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

