# read txn.txt file
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/txn.txt")
df.columns=["oid","date","cid","amount","product","category","city","state","method"]
print(df.to_csv())