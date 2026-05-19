import pandas as pd

data = {
    "Name": ['Nahid','Mashuk','Pranjol','Mahmuda','Sazon'],
    "Age" : [10,20,30,25,80],
    "City": ['Dhaka','Cumilla','Barishal','Pabna','Tangail']
}

df = pd.DataFrame(data)

print('Displaying the into of data set')
print(df.info())