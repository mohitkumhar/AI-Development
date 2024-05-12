import matplotlib.pyplot as plt

x = ["python", "C", "c++", "java"]
y = [85,70,60,82]

plt.xlabel("Language", fontsize=15)
plt.ylabel("Popularity", fontsize=15)
plt.title("Analysis", fontsize=15)

color = ["y", "c", "m", "g"]
plt.bar(x, y, width=0.4, color=color, align='center', edgecolor='black', linewidth=2, linestyle=':', alpha=0.4, label="Analysis")
plt.legend()
plt.show()

# plt.xlabel("Language", fontsize=15): Adds a label to the x-axis of the plot. The label text is "Language" and it's displayed with a font size of 15.

# plt.ylabel("Popularity", fontsize=15): Adds a label to the y-axis of the plot. The label text is "Popularity" and it's displayed with a font size of 15.

# plt.title("Analysis", fontsize=15): Sets the title of the plot to "Analysis" with a font size of 15.

# color = ["y", "c", "m", "g"]: Defines colors for each bar in the bar chart. Here, 'y' stands for yellow, 'c' for cyan, 'm' for magenta, and 'g' for green.

# plt.bar(x, y, width=0.4, color=color, align='center', edgecolor='black', linewidth=2, linestyle=':', alpha=0.4, label="Analysis"): Creates a bar chart using the data in x (labels) and y (values). The bars have a width of 0.4 and are colored according to the color list. Bars are centered (align='center'), have black edges (edgecolor='black') with a thickness of 2, and a dotted line style (linestyle=':'). The bars are slightly transparent (alpha=0.4). Each bar is labeled as "Analysis" for the legend.

# plt.legend(): Shows a legend on the plot based on the label specified in plt.bar(), which is "Analysis" in this case.

# plt.show(): Displays the plot on the screen.



# DOUBLE GRAPH

import matplotlib.pyplot as plt

x = ["python", "C", "c++", "java"]
y = [85,70,60,82]
z = [20,30,40,50]   # defines another set of values z representing a second set of data to be plotted as the heights of the second set of bars.

plt.xlabel("Language", fontsize=15)
plt.ylabel("Popularity", fontsize=15)
plt.title("Analysis", fontsize=15)

plt.bar(x,y,width=0.4, color='y', label='popularity')
plt.bar(x,z,width=0.4, color='r', label='popularity1')   # it creates a second set of bars using the data from x (labels) and z (values). The bars have a width of 0.4 and are colored red (color='r'). Each bar is labeled as "popularity1" for the legend.

plt.legend()
plt.show()


# Grouped Bar Chart

import matplotlib.pyplot as plt
import numpy as np

x = ["python", "C", "c++", "java"]
y = [85,70,60,82]
z = [20,30,40,50]

width = 0.2   # Sets the width of each bar in the bar chart.
p = np.arange(len(x))   # Creates an array p containing positions for the first set of bars based on the number of elements in x.
p1 = [j + width for j in p]   # Calculates positions for the second set of bars, offset from the first set by width.

plt.xlabel("Language", fontsize=15)
plt.ylabel("Popularity", fontsize=15)
plt.title("Analysis", fontsize=15)

plt.bar(p,y,width, color='y', label='popularity')   #  Plots the first set of bars (y) at positions p, colored yellow ('y') and labeled as "popularity".
plt.bar(p1,z,width, color='r', label='popularity1')  # Plots the second set of bars (z) at positions p1 (offset positions), colored red ('r') and labeled as "popularity1".

plt.xticks(p + width/2, x, rotation=20)   # Sets the positions and labels of the x-axis ticks. The positions (p + width/2) are adjusted to center the ticks under each pair of bars, with labels (x) representing the language names. The rotation=20 parameter rotates the labels by 20 degrees for better readability.
plt.legend()
plt.show()


# Horizontal BarGraph
import matplotlib.pyplot as plt

x = ["python", "C", "c++", "java"]
y = [85,70,60,82]
z = [20,30,40,50]

plt.xlabel("Language", fontsize=15)
plt.ylabel("Popularity", fontsize=15)
plt.title("Analysis", fontsize=15)


plt.barh(x,y, color='y', label='popularity') # this barh() creates a horizontal bar graph
plt.barh(x,z, color='r', label='popularity1')

plt.legend()
plt.show()