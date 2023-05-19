# iloc used to index based row
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/customer.csv")
print(df)
x=df.iloc[:,:-1] #iloc[rows : ,cols:-1]
y=df.iloc[:,-1] # iloc [rows:,cols-1]
print()
print(x)
print()
print()
print(y)

# print(dir)
