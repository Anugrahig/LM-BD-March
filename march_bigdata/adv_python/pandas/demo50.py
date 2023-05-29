# if Calories >:400
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
df.dropna(inplace=True)
mean_x=df["Calories"].mean()
print(mean_x)
df["Calories"]=df["Calories"].apply(lambda x: round(df["Calories"].mean(),2) if x>=400 else x)
print(df)