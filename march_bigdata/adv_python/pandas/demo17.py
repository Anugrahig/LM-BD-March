import pandas as pd
import numpy as np
df=pd.read_csv("./Files/Temperature",sep=" ")
df.columns=["year","temperature"]
print(df)