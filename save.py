import pandas as pd

data = {
    "Name": ['Nahid','Mashuk','Pranjol','Mahmuda','Sazon'],
    "Age" : [10,20,30,25,80],
    "City": ['Dhaka','Cumilla','Barishal','Pabna','Tangail']
}

df = pd.DataFrame(data)
print(df)

df.to_excel("output.xlsx",index=False) 