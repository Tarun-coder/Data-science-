# 1 2 3 4 -8 -10
from numpy import *

simple=array([1,2,3,4,-8,-10],dtype=float)
reverse=simple[::-1]
print(reverse)

a=arange(0,6,2)
print(a)
print(zeros((2,4)))

print(__version__)
print(show_config())
print(info(add))
print(all(a))
print(any(a))
print(full_like(a,4))
print("----------------------------")

print(random.randint(1,7,(4,3))[1:3,1:])
b=arange(0,11,2).reshape((3,2))
print(b)

print(random.random((4,3)))
print(eye(3,3,dtype=int))
print(identity(3))

print(random.randint(0,2,10))
# Random number bt 0 and 1
print(random.normal(0,1))

print("----------------------------")
b=random.randint(0,2,36).reshape(6,6)
print(b)
for i in nditer(b):
    print(i,end=" ")
print()    
print(b[0:2,0:2])
print(b[0:2,0:2].sum())

