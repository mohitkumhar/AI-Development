import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.step(x, y, color='r', marker='o', ms=10, mfc='g', label='Step - Plot') # all Linear Plot parameter can be applied on this Step Plot

# marker='o': This specifies the shape of the markers at the data points. ('o' means circle markers)
# ms=10: This sets the marker size to 10.
# mfc='g': This sets the marker face color to green

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Moiht's Step")

plt.legend()
plt.grid()
plt.show()