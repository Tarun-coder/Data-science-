from numpy import *
from sys import *
a=arange(5)
b=arange(3,8,1)
print(a)
print(b)
c=union1d(a,b)
print(c)
print(tile(c,2)) # tile function generate a repeating array with number of time given as 2nd input
# in above case it repeat array c array 2 times.
print(repeat(c,3)) # it repeat each element of array 3 times as given in repeat value
print(argmax(c))
print(argmin(c))
print("array lenth or size along with byte consumed by one element and byte consumed by all element in array")
b=[]
c=2
print("c:",c.__sizeof__())
print("c:",getsizeof(c))
print("b:",b.__sizeof__())
print(getsizeof(b))
a=[4,2]
print("a:",a.__sizeof__())
print(getsizeof(a))

print("memory address of list",id(a))
print("address of element in list:",id(4),"-----------",id(5))
n={5:"hello",6:"jain"}
print(id(n),"------",id(5),"----------------",id("hello"))

d=arange(5)
print(id(d),id(d[0]),id(d[1]),id(d[2]))
print(d.__sizeof__())
print(getsizeof(d))
print(getrefcount(d))
s=array([0,1,2,3,4,5])
print(getsizeof(s))
print(s.itemsize)
z=[1,1,5,3,4,5]
print(getsizeof(z[2])*len(z))
print(getsizeof(1))

# now all numpy array operation is going to performed

# concatenate two numpy array
a=arange(6).reshape((2,3))
print("The first array:",a)
b=arange(6,12,1).reshape((2,3))
print("The 2nd array is:",b)
print("concatenate array")
c=concatenate((a,b),1)
print(c)
print(getrefcount(c))





