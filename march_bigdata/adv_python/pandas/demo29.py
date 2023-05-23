# drop duplicate values : drop_duplicate()
import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
print(df)
x=df.iloc[:,:-1].values # values used for getting array of values (2D)
y=df.iloc[:,-1].values
print(x)
print()
print(y)
# duplicate value remove: duplicate rows will be remove (drop_duplicate)
print(df.shape)
df1=df.drop_duplicates()
print(df1.shape)

