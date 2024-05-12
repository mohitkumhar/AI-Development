# DataFrame: it is a 2-D data structure like 2-D array with table including rows and columns 

import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20,30,40]}
df = pd.DataFrame(data)
print(df)



# locate row: pandas use the loc attribute to return one or more specified row.
import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20,30,40]}
df = pd.DataFrame(data)
print(df.loc[0])



# example of returning row 0 and 1
import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20,30,40]}
df = pd.DataFrame(data)
print(df.loc[[0, 1]])
print()


# named index: with the index arg, you can name your own index
import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20, 30, 40]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)



# locate the name index:
import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20, 30, 40]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc["day1"])  # output in series
print()


# output in dataframe:
import pandas as pd
data = {"cal": [101, 102, 103], "duration": [20, 30, 40]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc[["day1", "day2"]])     # output in dataframe


# load data from csv file into dataframe i.e data.csv
fileload = pd.read_csv("data.csv")
print(fileload)
