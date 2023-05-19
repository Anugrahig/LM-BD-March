# iloc used to index based row
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/Temperature",sep=" ",names=["year","temperature"])
df1=df.rename(columns={"temperature":"temp"})
print(df1.iloc[5:12])
print()
print(df1.iloc[3]) #3rd index 4th row
print()
print(df1.iloc[:10])
print()
print(df1.iloc[10:]) #10 th index to last index
