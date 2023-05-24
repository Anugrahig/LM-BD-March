import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
print(df.head())
print()
# order
# where,loc,sort,column,header :order
#india Each prof count desc order
df1=df.loc[df["loc"]=="india"].groupby("prof")[["prof"]].count().sort_values(ascending=False)
print(df1)
print()



