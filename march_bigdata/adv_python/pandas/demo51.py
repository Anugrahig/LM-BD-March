# Max pulse above 122
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
print()
x=df["Maxpulse"].mean()
for y in df.index:
    if df.loc[y,"Maxpulse"]>122:
        df.loc[y,"Maxpulse"]=x
print(df)