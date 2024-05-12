# Pandas Series is like a column in a table, it is 1-D array which holds data of any type


# to create a simple pandas series
import pandas as pd
x = [1,2,3]
new_x = pd.Series(x)
print(new_x)



# labeling - label can be use access a specified value
import pandas as pd
x = [1,2,3]
new_x = pd.Series(x)
print(new_x[0])



# with Create label we can create our own label
import pandas as pd
x = [1,2,3]
new_x = pd.Series(x, index=["x", "y", "z"])
print(new_x["y"])



# we can also use a key or value object like a dictionary, when creating a series.

# to create a simple pandas series from a dictionary
import pandas as pd
x = {"day1": 101, "day2": 102, "day3": 103}
new_x = pd.Series(x)
print(new_x)



# now we will create a series using only data from day1 and day2
import pandas as pd
x = {"day1": 101, "day2": 102, "day3": 103}
new_x = pd.Series(x, index=["day1", "day2"])
print(new_x)


# DataFrame: Data sets in pandas are usually multidimensional series, and they are called DataFrames.

# Series are like Columns and DataFrame is the whole Tables.

# we will now create a dataframe from 2 series
import pandas as pd
x = {"cal": [101, 102, 103], "duration": [20, 30, 40]}
new_x = pd.DataFrame(x)
print(new_x)
