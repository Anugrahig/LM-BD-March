# based on condition we decide joining
import pandas as pd
import numpy as np
df1=pd.read_csv("Files/hr_data1.csv")
df2=pd.read_csv("Files/hr_data2.csv")
print(df1.head())
print(df2.head())
print("****")
df=pd.merge(df1,df2,on="Candidate_id")
# df=pd.merge(df1,df2,on="Candidate_id")
# 1. inner join, age above 34 , candtate_id,DOJ,status
print("1")
df3=df.loc[df["Age"]>34][["Candidate_id","DOJ_Extended","Status","Age"]]
print(df3)
# 2. status = joined , c_id,notic_peroid,Band
print("2")
df=pd.merge(df1,df2,on="Candidate_id",how="right")

df3=df.loc[df["Status"]=="Joined"][["Candidate_id","notice_period","Band"]]
print(df3)

# 3 band=E3, age location,candate_id,staus,band
print("*3*")
df=pd.merge(df1,df2,on="Candidate_id",how="left")

df3=df.loc[df["Band"]=="E3"][["Candidate_id","Age","Location","Status","Band"]]
print(df3)
# 4.(notice peroid =14 and age>34) full data
print("*4*")
df=pd.merge(df1,df2,on="Candidate_id",how="outer")

df3=df.loc[(df["notice_period"]>=14)&(df["Age"]>=34)]
print(df3.head())
#5 relocate =No , offer letter>100 ,id,offer_letter,status
print("5")
df=pd.merge(df1,df2,on="Candidate_id",how="left")

df3=df.loc[(df["Relocate"]=="No")&(df["offer_letter"]>100)][["Candidate_id","offer_letter","Status"]]
print(df3)

print(6)
df3=df.loc[(df["notice_period"]>=14)&(df["Age"]>=34)].sort_values(by="Age",ascending=False)
print(df3)

"""
Index(['Candidate_id', 'DOJ_Extended', 'offer_letter', 'notice_period', 'Band',
       'Relocate'],
      dtype='object') Index(['Candidate_id', 'Gender', 'Source', 'Location', 'Age', 'Status'], dtype='object')
"""
