# cleaning data: it means fixing the bad data in your data set.
# Bad data could be: empty cell, data in a wrong format, duplicate data and wrong data.
# empty cell: it will give you wrong result always, we have to remove the rows always that contain the bad data

# loading and reading the original dataframe
import pandas as pd
x = pd.read_csv("data.csv")
print(x.to_string())



# to remove the rows containing the NULL(NaN) values use - dropna()

# create new data frame with no empty cell, 
import pandas as pd
x = pd.read_csv("data.csv")
new_x = x.dropna() # will not change original dataframe
print(new_x.to_string())


# to change the original dataframe, then use the inplace=True argument.
import pandas as pd
x = pd.read_csv("data.csv")
x.dropna(inplace=True)
print(x.to_string())


# replacing the empty value: we will use the fillna() method which will allow us to replace the empty cell with a value
import pandas as pd
x = pd.read_csv("data.csv")
x.fillna(130, inplace=True)
print(x.to_string())


# to replace only the empty value for one column, you need to specify the column name
import pandas as pd
x = pd.read_csv("data.csv")
x['Data_value'].fillna(130, inplace=True)
print(x.to_string())



# to replace the empty cell with mean(), median() or mode()

# calculate the MEAN and replace the empty values with it
import pandas as pd
x = pd.read_csv('data.csv')
new_x = x["Data_value"].mean()
x['Data_value'].fillna(new_x, inplace=True)
print(x.to_string())


# calculate the MEDIAN and replace any empty values in it
import pandas as pd
x = pd.read_csv("data.csv")
new_x = x['Data_value'].median()
print(x.to_string())
x['Data_value'].fillna(new_x, inplace=True)
print(x.to_string())



# calculate the MODE and replace any empty values in it
import pandas as pd
x = pd.read_csv("data.csv")
new_x = x["Data_value"].mode()[0]
x["Data_value"].fillna(new_x, inplace=True)
print(x.to_string())
