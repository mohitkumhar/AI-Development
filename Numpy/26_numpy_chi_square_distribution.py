# Chi Square Distribution - it is basically used as a basis to verify the hypothesis.

# param - df(degree of freedom), size(shape of returned array)

# sample for a chisquared distribution with df 2 with size 2*3
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)


# visualisation of chisquare
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=11, size=(2,3)), hist=False)
plt.show()


