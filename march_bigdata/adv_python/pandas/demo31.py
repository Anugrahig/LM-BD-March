# Evaluating Functions
# Count
# Max
# Min
# Sum
# Average
import pandas as pd
import numpy as np
df=pd.read_csv("Files/sample4.txt",names=["id","fname","lname","age","num","loc"])
print(df.head())
print()
# count():count each column count
# ---------
# df1=df.groupby("colname") [colname].count()
df1=df.groupby("loc")["loc"].count()
print(df1)


