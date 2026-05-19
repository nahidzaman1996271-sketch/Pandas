# head() tail()
# head() 5
# tail(n) 5

import pandas as pd

df = pd.read_excel("D:\Pandas\sample_data.xlsx")
print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))
