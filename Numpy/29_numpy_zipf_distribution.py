# Zipf distribution - common word in english has occure nearly 1/5 time as of the most hindi words

# param = a(distrution paramater), size


# sample for zipf(distribution), with a as 2 with size 2*3
from numpy import random
x = random.zipf(2, size=(2,3))
print(x)



# visualisation of zipf distrubution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.zipf(a=2, size=1000), hist=False)
plt.show()



