'''
1- how big is your dataset?
2- What are the names of columns

shape and columns
'''
# step-1 sample data frame

import pandas as pd

data = {
    "Name": ['Nahid','Ibn','Zaman','Ikfa','Symooon'],
    "Age": [10,20,30,40,50],
    "Salary": [900000,5000,6000,40000,100000],
    "Performance Score": [20,50,60,40,15]
}

df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column names: {df.columns}')

'''
(1000,10)
'''