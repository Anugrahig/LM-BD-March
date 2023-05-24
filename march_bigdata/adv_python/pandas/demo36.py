import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer5.txt",names=["id","fname","lname","age","prof","loc","sal"])
print(df.head())
# each prof count [count desc]
print()
df1=df.groupby("prof")["prof"].count().sort_values(ascending=False)
print(df1.head(10))
# each prof max salery
df1=df.groupby("sal")["prof"].max()
print(df1)
# each loc min salery
print()
df1=df.groupby("sal")["loc"].min()
print(df1.head())
print()
# each prof avg salery
# df1=df.groupby("sal")["prof"].mean()
df1=df.groupby("prof")["sal"].mean()
print(df1.head())
print()
# each loc tot sale
df1=df.groupby("loc")["sal"].sum()
print(df1.head())
print()
# each prof total salery
df1=df.groupby("prof")["sal"].sum()
print(df1.head())