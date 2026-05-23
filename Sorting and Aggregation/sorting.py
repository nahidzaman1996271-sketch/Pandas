# sorting data
# SORTING DATA 1 COLUMN sort_values()
# df.sort_values(by = "Column Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name":['Nahid','Ibn','Zaman'],
    "Age": [28,4,5],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age",ascending=False,inplace=True)
print("Sorted by descending:")
print(df)