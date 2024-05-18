# fill_between()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.plot(x,y,color='r')

plt.fill_between(x,y, color='green', where=(x >= 2) & (x <= 4), alpha=0.4)  #where=(x >= 2) & (x <= 4): This specifies the condition under which the area between the x-axis and the plot will be filled. In this case, the fill will only occur where the x values are between 2 and 4 (inclusive).


# or the values of x and y can also be given directly for simple graph

plt.fill_between(x=(2,3),y1=2,y2=3, color='green', alpha=0.4)

# x=(2,3): This specifies the range of x-values over which you want to fill the area. In this case, the fill will occur between x = 2 and x = 3.

# y1=2: This sets the lower boundary of the filled area on the y-axis. The fill will start at y = 2.

# y2=3: This sets the upper boundary of the filled area on the y-axis. The fill will extend up to y = 3

plt.show()