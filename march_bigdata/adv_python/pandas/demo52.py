# fill missing values
# date :random date
# distance :mean
# avgMovingSpeed : median()
# Fuel economy : mode

import pandas as pd
import numpy as np
df=pd.read_csv("Files/travel-times.csv")
print(df.isna().sum())
print(df.columns)
print()
print(df)
df["Date"].fillna("20-02-2022",inplace=True)
print(df)
print()
print("2")
x=df["Distance"].mean()
df["Distance"].fillna(x,inplace=True)
print(df.isna().sum())
print(df)
print(df.isna().sum())
print("3")
df["AvgMovingSpeed"].fillna(df["AvgMovingSpeed"].median(),inplace=True)

print()
print(df)
print(df.isna().sum())
df["FuelEconomy"].fillna(df["FuelEconomy"].mode()[0],inplace=True)
print()
print(df)
print(df.isna().sum())
print()
"""

'Date', 'StartTime', 'DayOfWeek', 'GoingTo', 'Distance', 'MaxSpeed',
       'AvgSpeed', 'AvgMovingSpeed', 'FuelEconomy', 'TotalTime', 'MovingTime',
       'Take407All'],

"""

