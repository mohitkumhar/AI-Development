# Scatter Plot
import matplotlib.pyplot as plt

day = [1,2,3,4,5,6,7]
no = [2,3,1,4,5,3,6]

colors = ['r', 'b', 'g', 'y', 'purple', 'orange', 'cyan']
size = [100,20,40,50,20,100,70]

plt.scatter(day, no, c=colors, s=size, alpha=0.6, marker='*', edgecolor='g', linewidth=0.4)
# 'day' and 'no' are lists representing the x and y coordinates of the scatter plot points.
# 'c=colors' assigns colors to each point based on the colors list.
# 's=size' sets the size of each point based on the size list.
# 'alpha=0.6' controls the transparency of the points (0 = fully transparent, 1 = fully opaque).
# "marker='*'" specifies that each point should be displayed as a star (*).
# "edgecolor='g'" sets the color of the edges (outlines) of the markers to green.
# "linewidth=0.4" determines the width of the marker edges.




plt.title("Scatter Plot", fontsize=15)   # Sets the title of the plot to "Scatter Plot" with a font size of 15.
plt.xlabel("Day", fontsize=15)   # Sets the label for the x-axis to "Day" with a font size of 15.
plt.ylabel("No", fontsize=15)   # Sets the label for the y-axis to "No" with a font size of 15.

t = plt.colorbar()   # Adds a color bar to the plot, which corresponds to the colors (c) used in the scatter plot.
t.set_label("Color Bar", fontsize=23)   # Sets the label for the color bar to "Color Bar" with a font size of 23.

plt.show()




# Multiple Scatter Plot
import matplotlib.pyplot as plt

day = [1,2,3,4,5,6,7]
no = [2,3,1,4,5,3,6]
no2 = [3,2,4,5,1,6,2]

colors = ['r', 'b', 'g', 'y', 'purple', 'orange', 'cyan']
size = [100,20,40,50,20,100,70]

plt.scatter(day, no)   # Plots a scatter plot with points represented by day on the x-axis and no on the y-axis. Each point is colored based on the default color scheme.
plt.scatter(day, no2)   # Plots another set of scatter points with day on the x-axis and no2 on the y-axis. These points are also colored based on the default color scheme, creating a second set of data on the same plot.

plt.title("Scatter Plot", fontsize=15)
plt.xlabel("Day", fontsize=15)
plt.ylabel("No", fontsize=15)

t = plt.colorbar()
t.set_label("Color Bar", fontsize=23)

plt.show()

# The rest of the code (plt.title(), plt.xlabel(), plt.ylabel(), t = plt.colorbar(), t.set_label(), plt.show()) remains the same as Previous one