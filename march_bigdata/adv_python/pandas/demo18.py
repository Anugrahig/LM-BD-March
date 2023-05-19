# rename column names
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
df1=df.rename(columns={"prof":"dept"})
print(df1.head())