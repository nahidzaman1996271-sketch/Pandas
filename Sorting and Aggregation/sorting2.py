# df.sort_values(by=["Age","Salary"], ascending = True, inplace = True)

import pandas as pd

data = {
    "Name":['Nahid','Ibn','Zaman'],
    "Age": [28,4,5],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age","Salary"], ascending=[True,False],inplace=True)
print("Sorted by descending:")
print(df)