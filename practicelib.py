# It will print 5x5 matrix 
import numpy as np

a=np.ones((5,5))
print(a)
print("---------------------------------------")
a[1,1:4]=[0,0,0]
a[3,1:4]=[0,0,0]
a[2,1:4]=[0,9,0]

print(a)

a=np.full((5,5),4)
print(a)

b=np.eye(3,3)
print(b)
b=np.matrix(b)
print(b.diagonal())

print("---------------------practice numpy-------------------------")

a=np.arange(1,11)
a=a.reshape(2,5)
print(a)
print()
b=np.arange(11,21)
b=b.reshape(2,5)
print(b)
print()
c=np.concatenate((a,b))
c=np.array(c)
print(c.shape)
d=a+b
print(d)
d=15/d
print(d)
