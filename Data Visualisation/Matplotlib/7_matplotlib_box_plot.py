# Box Plot
import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70, 120]

plt.boxplot(x, notch=True, vert=True,labels=['a'], widths=0.2, patch_artist=True, showmeans=True, sym='g+', boxprops={'color':'r'},  
            capprops={'color':'g'}, whiskerprops={'color':'r'},
           flierprops={'markeredgecolor':'y'})

# notch=True: Adds a small cut in the box showing where the median is.

# vert=True: Shows the plot from top to bottom.

# widths=0.2: Makes the boxes narrower.

# patch_artist=True: Fills the boxes with color.

# showmeans=True: Puts a dot in the box to show the average.

# sym='g+': Uses green crosses to show any unusual values.

# boxprops={'color':'r'}: Makes the box outline red.

# capprops={'color':'g'}: Makes the ends of the whiskers (lines) green.

# whiskerprops={'color':'r'}: Makes the whisker lines red.

# flierprops={'markeredgecolor':'y'}: Outlines unusual value markers with yellow.


plt.show()



# Multiple Box Plot
import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70, 120]
x1 = [10,20,40,50,30,60,90]

y = [x,x1]

plt.boxplot(y)


plt.show()
