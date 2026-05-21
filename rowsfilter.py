import pandas as pd

data = {
    "Name": ['Nahid','Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,20,30,40,50],
    "Salary": [900000,5000,6000,40000,100000],
    "Performance Score": [20,50,60,40,15]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print("Employees with salary > 50000")
print(high_salary)

# filtering rows salary > 50k & age > 30
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print(f'Employee list age > 30 and + salary > 50000')
print(filtered)
# using or condition
filtered_or = df[(df['Age'] > 35) | (df["Performance Score"] > 90)]
print('Employees older than 35 OR performance score > 90')
print(filtered_or)