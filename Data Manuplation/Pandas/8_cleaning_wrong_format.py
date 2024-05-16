# data in a wrong format: to fix this problem, there are 2 ways: removing the rows or convert all the cell in the same format

# to convert all the cells in the data column into dates. via to_datetime()
import pandas as pd
x = pd.read_csv('data.csv')
x['Date'] = pd.to_datetime(x['Date'])    # it changes 20201226 to 2020/12/26
print(x.to_string())


# to remove rows with a NULL value in the 'Date' column.
import pandas as pd
x = pd.read_csv('data.csv')
x['Date'] = pd.to_datetime(x['Date'])
x.dropna(subset=['Date'], inplace=True)
print(x.to_string())



