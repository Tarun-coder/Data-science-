from numpy import *
from pandas import *

df=read_csv("dataset.csv")
df1 = DataFrame({'Python': [12, 43, 54, 16, 63], 'C': [32, 56, 23, 67, 21], 'Java': [23, 56, 63, 45, 52]}, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(df)
print(df.head(3))
print(df.info())
print(df.isnull())
print(df.describe())
print(df["Cost"])
print(df.loc[1:9,"Cost":])
df2=concat([df,df1])
print(df2)

print(df2.isnull().sum())
df2["Java"]=df2["Java"].fillna(df2["Java"].mean())
print(df2["Java"])

a=arange(4)
print(a)
a[:]=1
print(a)
