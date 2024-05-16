# wrong data: its only a wrong data


# loading and reading the original dataframe
import pandas as pd
x = pd.read_csv('data.csv')
print(x.to_string())

# to set "Date" 
import pandas as pd
x = pd.read_csv("data.csv")
x.loc[3, 'Date'] = 12122004
print(x.to_string())


# for larger dataset: we loop through all the values in "Data_value" column, if the value is higher than 120 then set it to 200
import pandas as pd
x = pd.read_csv("data.csv")
for i in x.index:
    if x.loc[i, 'Data_value'] > 90000:
        x.loc[i, 'Data_value'] = 200
print(x.to_string())


# to remove the rows for wrong data in larger dataset
import pandas as pd
x = pd.read_csv('data.csv')
for i in x.index:
    if x.loc[i, 'Data_value'] > 90000:
        x.drop(i, inplace=True)
        
print(x.to_string())        
        


        

