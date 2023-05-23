# drop() delete  column:
import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
df1=df.drop(["prof"],axis=1)
print(df1.head())
print()
df1=df.drop(["prof","loc"],axis=1)
print(df1.head())
