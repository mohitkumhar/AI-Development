# removing the duplicate values: first we need to discover the duplicate values via duplicate() method.


# returns Trur for every 
# w that is duplicate otherwise return False:
import pandas as pd
x = pd.read_csv("data.csv")
print(x.to_string())
print(x.duplicated().to_string())



# removing the duplicate from the data set via drop_duplicates()
import pandas as pd
x = pd.read_csv("data.csv")
x.drop_duplicates(inplace=True)
print(x.to_string())

