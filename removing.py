import pandas as pd

data = {
    "Name": ['Nahid','Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,20,30,40,50],
    "Salary": [90000,5000,6000,40000,10000],
    "Performance Score": [20,50,60,40,15]
}

df = pd.DataFrame(data)
print(df)

print('\n\nModified Data:')
df.drop(columns=["Performance Score"], inplace=True)
print(df)