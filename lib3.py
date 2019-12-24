from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *

li=[("Rahul",22),("Rohit",23),("Jay",20)]
df=DataFrame(data=li,columns=["Name","Age"],index=[0,1,2])
print(df)

#print(df.loc["A",["Name","Age"]])
c=array([2,3,4,5,6,7,8,9])
print(c)
print(df["Age"])

print(df.loc[df["Age"]>20])
print(df.loc[df["Age"].index,"Name"])
df["Weight"]=[12,13,45]
print(df)

print(df["Weight"].index)
print(df[0:2])
d=c.reshape(2,2,2)
print(d)

print(df.info())
print(df.boxplot())
print(df.hist())
df.to_csv("dataframe.csv",sep=",",index=False)

print(df.isnull().sum())

nf=read_csv("hello.csv",sep=",")
print(nf)
print(nf.shape)
print(nf.info()) # The number of values each coloumn have

cn=df+nf
print(cn)


a=arange(1,10,1)
print(a.itemsize*len(a))
b=range(1,10,1)
print(b.__sizeof__())

print(type(nf))


