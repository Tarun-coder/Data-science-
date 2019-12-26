from pandas import *
from numpy import *
# single coloumns data structure in pandas is series. it contain single coloumns
li=[("Rahul",22),("Rohit",23),("Jay",20)]
df=DataFrame(data=li,columns=["Name","Age"],index=[("abc")])



