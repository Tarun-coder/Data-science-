# It will print 5x5 matrix 
import numpy as np

a=np.ones((5,5))
print(a)
print("---------------------------------------")
a[1,1:4]=[0,0,0]
a[3,1:4]=[0,0,0]
a[2,1:4]=[0,9,0]

print(a)