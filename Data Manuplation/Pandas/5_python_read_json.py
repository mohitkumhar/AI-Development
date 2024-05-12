# JSON: Big data sets are normally stored and extracted as JSON. JSON is a plain text, but it has a format of an object.

# loading the JSON into a dataframe
import pandas as pd
data = pd.read_json('data.json')
print(data.to_string())


# dictionary as a JSON: if our JSON code is not in a file but in a python dictionary, then we can do all below:
data = {
    "Person1":
        {
            "firstName": "Joe",
            "lastName": "Jackson",
            "gender": "male",
            "age": 28,
            "number": "7349282382",
        },

        "Person2":
        {
            "firstName": "James",
            "lastName": "Smith",
            "gender": "male",
            "age": 32,
            "number": "5678568567"
        },

        "Person3":
        {
            "firstName": "Emily",
            "lastName": "Jones",
            "gender": "female",
            "age": 24,
            "number": "456754675"
        },
    }

df = pd.DataFrame(data)
print(df)