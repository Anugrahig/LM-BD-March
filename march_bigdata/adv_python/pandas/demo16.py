import pandas as pd
import numpy as np
df=pd.read_csv("./Files/patent",sep=" ")
df.columns=["patent","sub patent"]
print(df)