# Pie Plot


import matplotlib.pyplot as plt

x = [10,20,30,40]
y = ['c', 'cpp', 'java', 'python']
explode = [0.3, 0.0, 0.0, 0.0]

c = ['r', 'b', 'g', 'y']

plt.pie(x, labels=y, explode=explode, autopct="%0.1f%%", shadow=True, radius=0.8, labeldistance=1, startangle=0, textprops={"fontsize":15}, counterclock=False, wedgeprops={'linewidth':2, 'width':0.8, 'edgecolor':'m'}, center=(0,0), rotatelabels=True)

# Explode: Determines how much each wedge is pulled out from the center. The first value (0.3) makes the first wedge ('c') stand out more.

# Autopct: Formats the labels inside the wedges to show the percentage of each slice with one decimal place.

# Shadow: Adds a shadow effect behind the pie chart.

# Radius: Sets the size of the pie chart (0.8 means it's slightly smaller than the default size).

# Labeldistance: Controls the distance of the labels from the center of the pie.

# Startangle: Specifies the starting angle for the first wedge (0 degrees starts at the right side).

# Textprops: Sets properties for the text labels inside the pie slices, such as font size.

# Counterclock: Determines if the slices are drawn in a counterclockwise direction (False means clockwise).

# Wedgeprops: Controls the appearance of the pie wedges, including line width, width of the wedge, and edge color.

# Center: Positions the pie chart at the center of the figure (in this case, at coordinates (0,0)).

# Rotatelabels: Rotates the labels inside the wedges to align with the starting angle.


plt.title("Mohit's Pie")

plt.legend(loc=2)   # Adds a legend to the pie chart based on the labels (y) of the slices.
plt.show()



# Dot PieChart

plt.pie([1])
plt.show()  # This creates a simple pie chart with a single wedge representing 100% (the whole pie).



# DoNut Pie Chart

import matplotlib.pyplot as plt

x = [10,20,30,40]
x1 = [40,30,20,10]
t = ['c', 'cpp', 'java', 'python']
plt.pie(x, labels=y, radius=1.5)
plt.pie([1], colors='w') # call adds a small white wedge ([1] with colors='w') to the center, creating a hole in the middle and transforming the pie into a donut shape.

plt.show()




# Another DoNut Pie Chart
import matplotlib.pyplot as plt

x = [10,20,30,40]
x1 = [40,30,20,10]
y = ['c', 'cpp', 'java', 'python']

# Create a pie chart with specified data, labels, and radius
plt.pie(x, labels=y, radius=1.5)

# Create a white circle to make a hole in the center (creating a donut shape)
cr = plt.Circle(xy=(0,0), radius=1, facecolor='w')   # Create a white circle

# plt.Circle(): Constructs a white circle (facecolor='w') with a radius of 1, which will be placed at the center of the pie chart. This creates a hole in the center, transforming the pie chart into a donut shape.



plt.gca().add_artist(cr)   # Add the circle to the current Axes
# plt.gca().add_artist(): Adds the created white circle (cr) to the current Axes of the plot. This is necessary to overlay the circle onto the existing pie chart.


plt.show()

