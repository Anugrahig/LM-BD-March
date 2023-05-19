# rename column names
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/Temperature",sep=" ",names=["year","temperature"])
df1=df.rename(columns={"temperature":"temp"})
print(df1.head())