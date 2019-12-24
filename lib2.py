from pandas import *
from numpy import *

a=DataFrame({"Name":["a","b","c","d"],"Roll No":[23,24,67,89],"Mark":[56,74,78,79]})
b=DataFrame({"chr":["e","f","g","h"],"No":[29,39,49,59],"id":[49,74,68,99]})

print(a)
print(a.info())
print("-------------------------------2nd Sheet---------------------------")
print(b)


print(a.join(b))

b.to_csv("hello.csv",index=False)
print(b.to_numpy())
print(b.head(2))
print(a.columns)
a["Name"][2]="Tarun"
print("------------------------------")

print(a)
a.to_csv("myexcel.csv",index=False)

a.columns=list("ABC")
print(a)
print("--------------------------------")

a.loc[2,"A"]="c"
print("----------------")
print(a)
print("-----------------------------")
print(a.loc[1:2,"A":"B"])
print("------------")
print(a)
print("--------------")
print(a.iloc[0,2])
print("-----------")
print(a.drop([0,1]))
print("-----------------")
print(a["A":])