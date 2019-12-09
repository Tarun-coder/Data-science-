import numpy as np
import matplotlib.pyplot as pl
import random

print(pl.figure(4))
n=[1,"hello","bang",22,"new"]

a=np.array(n)
print(a.argmax())
print(a)
b=np.zeros((3,5)) # It will create one diamensional array of element containing 5 zeroes.
print(b)
c=np.eye(3) + np.eye(3) # np.eye(3) it create 3x3 identity matrix diagonal element 1 while all are zeroes.
print(c)
d=np.ones((3,5))
print(d)

g=np.linspace(1,2,20)
print(len(g))

print(np.random.rand(4))
print(np.random.rand(2,2))

p=np.ones(5)+np.ones(5)
print(p)

