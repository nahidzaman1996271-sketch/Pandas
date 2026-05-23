import pandas as pd

data = {
    "Name":['Nahid','Ibn','Zaman','Sagor','Sumon'],
    "Age": [28,44,35,56,19],
    "Salary": [50000,40000,60000,55000,48000]
}

df = pd.DataFrame(data)
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)