from numpy import *

a=array([[2,3,4,5,6],[4,5,6,4,6]])
print(type(a))
print(a.shape)
print(a.sum(axis=1),a.dtype)
print("The total array size is:",a.itemsize*a.size)
b=range(1,11,1)
print("The total list size is:",b.__sizeof__())
c=full((2,2),-1,dtype="float")
print(c.mean())

g=range(1,5,1)
print(type(type))
