# mathplotlib (pyplot) - seaborn

# seaborn is a library that uses matplotlib underneath to plot graph i.e. pyplot

# distplot - distribution plot(curve plot- histogram)


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()


# ploting a displot without the histogram
import matplotlib.pyplot as plt
import seaborn as sns
x = [0,1,2,3,4,5]
sns.distplot(x, hist=False)
plt.show()
