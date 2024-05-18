# Stack Plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
area1 = [2,3,2,5,4]
area2 = [2,3,4,5,6]
area3 = [1,3,2,4,2]

labels = ['area1', 'area2', 'area3']

plt.stackplot(x, area1, area2, area3, labels=labels, colors=['r','g','m'], baseline="zero")

# This function creates a stack plot using the data provided in x, area1, area2, and area3.

# The x values represent positions on the x-axis.

# area1, area2, and area3 are lists containing the y-values for different areas to be stacked.

# baseline="zero" sets the baseline for stacking to zero.


plt.title("Mohit's Stack")
plt.xlabel("X-Label")
plt.ylabel("Y-Label")

plt.legend(loc=2)
plt.show()
