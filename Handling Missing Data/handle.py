# dropna()
# axis = 0 means the missings values in the rows will be deleted
# axis = 1 means the missings values in the columns will be deleted


import pandas as pd

data = {
    "Name": ['Nahid',None,'Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,None,20,30,40,50],
    "Salary": [90000,None,5000,6000,40000,10000],
    "Performance Score": [20,None,50,60,40,15]
}

df = pd.DataFrame(data)
print(df)

print("\n\nAfter removing the missing values:")
df.dropna(inplace = True)
print(df)