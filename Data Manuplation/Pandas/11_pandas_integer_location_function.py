# iloc = integer location function

# dataframe.iloc[row_index, column]


# selecting in single element
# val = dataframe.iloc[row_index, column]

# selecting a specific row
# val = dataframe.iloc[row_index]

# selecting a multiple row
# val = dataframe.iloc[startRow:endRow]

# selecting a specific row and column
# val = dataframe.iloc[[row1, row2], [col1, col2]]

# selecting a all rows for specific column
# val = dataframe.iloc[:, [col1, col2]]


# -X-X-X

# Example
import pandas as pd
data = {'name': ['mohit', 'heisenberg', 'qwerty', 'heisen'],
        'age': [19, 41, 23, 21],
        'country': ['india', 'canada', 'uk', 'austarlia']}

df = pd.DataFrame(data)

# selecting 'canada'
element = df.iloc[1,2]
print(element)

# selecting specific row and specific column
subset = df.iloc[1:3, 0:2]
print(subset)

