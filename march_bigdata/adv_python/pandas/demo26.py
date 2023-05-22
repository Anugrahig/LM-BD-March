# sorting
import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","pro","loc"])
# df1=df.sort_values(by="age",ascending=False)
df1=df.sort_values(by="age")
print(df1.head(10))