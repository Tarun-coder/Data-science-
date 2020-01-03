from numpy import *
from sys import *
a=ones((3,3))
print("original array is")
print(a)
print("array after adding 0 at original array")
a=pad(a,pad_width=2,mode="constant",constant_values=0)
print(a)

print("draw 8x8 matrix which is checkerboard")

b=zeros((8,8),dtype="int")
print(b)
b[0::2,1::2]=1
b[1::2,0::2]=1
print(b)
c=[3,4,5,6,7,8]
print(getsizeof(3)*len(c))



print(c)
n=array(c)
n=append(n,[10,20,30])
print(n)
f=(2,3,4,5,6,7,8,9,10)
g=array([f]).reshape(3,3)
print(g)

v=empty((3,4))
print(v)
d=full((3,4),4)
print(d)
print(d.itemsize*d.size)


