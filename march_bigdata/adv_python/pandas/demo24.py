import pandas as pd
import numpy as np
df=pd.read_csv("./Files/customer.csv",names=["id","fname","lname","age","loc"],nrows=50)
print(df.info())
print(df.isna().sum())
df1=df.fillna("uk")
print(df1.info())
print(df1.isna().sum())
x=df1.iloc[:,:-1]
y=df1.iloc[:,-1]
print()
print(x)
print(y)
print()
print(df1[["fname","age","loc"]])
