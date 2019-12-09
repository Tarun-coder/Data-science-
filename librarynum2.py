# We can create one diamensional numpy array aslo called as vector.
# Perform various operation on 1-d array.

#  Method to create numpy array 
import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9])
arr2=np.arange(12)
print(arr1)
print(arr2)
# operation on array
print(5*arr1)
arr1.shape=(3,3) # shape(rows,coloumn) it make array of given rows and coloumn
print(arr1)
print(arr1[0,0])
print(arr1.ndim)
# convert 2-d into 3-d array
arr2=arr2.reshape(2,2,3) # It is 3d array containing two 2d array that contain 2 row 3 coloumn each.
print(arr2)
print(arr2.ndim,arr2.size)
print()
print(arr2[0]*arr2[1])
print("------------matrix------------")
m=np.matrix(arr1)
print(m)
# matrix operation
print(m.transpose())

