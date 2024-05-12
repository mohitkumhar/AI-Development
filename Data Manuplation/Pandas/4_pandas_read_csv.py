# read csv files (comma seperated file) it is a simple way to store the big and biggest data sets
# csv files contain plain text

# loading csv into a dataframe with to_string()
import pandas as pd
data = pd.read_csv('data.csv')
print(data.to_string())


# loading csv into a dataframe without to_string()
import pandas as pd
data = pd.read_csv('data.csv')
print(data)


# max_rows: we can check our system's maximum rows with:
import pandas as pd
print(pd.options.display.max_rows)



# we can increase the number of rows to display the entire dataframe
import pandas as pd
pd.options.display.max_rows = 9999
data = pd.read_csv('data.csv')
print()
print(data)
