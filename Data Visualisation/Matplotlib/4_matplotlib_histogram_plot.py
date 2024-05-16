# Histogram Plot

import matplotlib.pyplot as plt
import numpy as np
import random


x = np.random.randint(10, 60, 50)
print(x)
l = [10,20,30,40,50]


plt.hist(x, color = 'r', edgecolor='black', bin=l, range=(10, 60), cumulative = -1, bottom=10, align='mid', histtype='barstacked', orientation='vertical', rwidth=0.8, log=False, label="Mohit's Histo")   # should use Either range or bin

# "bins": Determines how the data is divided into groups (bins) for the histogram. It can be specified as the number of bins or as an array defining the edges of the bins.

# "range": Sets the minimum and maximum values of the data range that will be included in the histogram. Data outside this range will not be shown.

# "cumulative": When set to -1, the histogram displays cumulative counts. Each bar shows the total count of data points up to that bin.

# "bottom": Sets the baseline (starting point) for the bars in the histogram. It shifts all bars up or down by this amount.

# "align": Controls the positioning of the bars relative to the bin centers. For example, 'left' aligns bars to the left of the bin center, 'mid' aligns them at the center, and 'right' aligns them to the right.

# "histtype": Specifies the style of histogram to draw. 'bar' creates standard bars, 'barstacked' stacks bars on top of each other, and 'step' draws a step histogram.

# "orientation": Determines whether the histogram is shown vertically (default) or horizontally.

# "rwidth": Adjusts the width of the bars relative to the bin width. A value of 1.0 means bars touch each other, while smaller values create gaps between bars.

# "log": If True, the histogram y-axis scale is logarithmic instead of linear. This is useful for visualizing data with a wide range of values.



plt.title("HistoGram")
plt.xlabel("Python")
plt.ylabel("No.")

plt.axvline(30, color='black', linestyle='--', alpha=0.8)   # Adds a vertical line at x=30 with color black

# color: Sets the color of the line.
# linestyle: Specifies the line style (e.g., solid, dashed, dotted).
# linewidth: Controls the width of the line.
# alpha: Sets the transparency (opacity) of the line.


plt.legend()

plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# color = 'gray' sets the color of the grid lines to gray.
# linestyle = '--' specifies a dashed line style for the grid lines.
# linewidth = 0.5 controls the width of the grid lines.
# alpha = 0.5 sets the transparency (opacity) of the grid lines.


plt.plot()


