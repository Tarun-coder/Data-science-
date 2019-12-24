from pandas import *
from numpy import *

df=DataFrame(data=[21,24,13,45],columns=["id"])
print

df["name"]=range(1,7)
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())

a=array([2,3,4,5,6])
print(a.shape)