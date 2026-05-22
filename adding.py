# adding columns
import pandas as pd

data = {
    "Name": ['Nahid','Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,20,30,40,50],
    "Salary": [900000,5000,6000,40000,100000],
    "Performance Score": [20,50,60,40,15]
}

df = pd.DataFrame(data)
# square brackets df["Column_Name"] = some_Data
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert()
# df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee ID", [10,20,30,40,50])
print(df)