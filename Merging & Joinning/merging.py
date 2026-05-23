# pd.merge(df1, df2, on = "Column_Name", how = "type of join")

import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Nahid','Ibn','Zaman']
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

# merge
df_merged = pd.merge(df_customers,df_orders, on="CustomerID", how="inner")
print("inner join")
print(df_merged)

# There is also so many functions like outer, left, right u just need to replace in the "how"