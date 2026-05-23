#fillna()
#fillna(value, inplace = True)

import pandas as pd

data = {
    "Name": ['Nahid',None,'Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,None,20,30,40,50],
    "Salary": [90000,None,5000,6000,40000,10000],
    "Performance Score": [20,None,50,60,40,15]
}

df = pd.DataFrame(data)
print(df)

df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)