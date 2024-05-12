# Viewing the data: one of the most used method for a quick overview of the dataframe is the head() method.

# This method returns the headers and a specified number of rows.

# to print data from 1st 10 rows in the dataframe
import pandas as pd
data = pd.read_csv("data.csv")
print(data.head(10))


# to print the last 10 rows in the datadframe
import pandas as pd
data = pd.read_csv("data.csv")
print(data.tail(10))



# what if we want the information about the data in dataframe: via info()
import pandas as pd
data = pd.read_csv("data.csv")
print(data.info())
