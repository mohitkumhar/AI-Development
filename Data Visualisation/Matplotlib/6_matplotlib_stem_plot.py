import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,2,5,6,3,3]

plt.stem(x, y, linefmt=':', markerfmt='r+', bottom=1, basefmt='g', label="Mohit's Stem", orientation='vertical')

# linefmt=':': it specifies the format of the stem lines. Here, it's set to a dotted line (':').

# markerfmt='r+': it specifies the format of the markers on the stems. Here, it's set to red crosses ('r+').

# bottom=1: it sets the bottom value of the stems. This can be a scalar or an array-like, defining the y-coordinate where the stems start.

# basefmt='g':it sets the format of the baseline.

# label="Mohit's Stem": it assigns a label to the stem plot, which can be used in legends.

# orientation='vertical': it specifies the orientation of the stems.



plt.legend()
plt.show()

