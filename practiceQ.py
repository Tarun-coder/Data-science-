# Write a Python program to create a tuple with numbers and print one item.
a=(2,3,4,5,6,7) # Tuple containing Number
print(a[0])

# Write a Python program to add an item in a tuple.
# Tuple is a
# To add an Item in the Tuple at specific location is given below
tuplex=a[0:2] + (9,3,2,) + a[2:]
print(tuplex)

# Tuple to String
b=("1","2","3","4") # Tuple must contain only character as element or numeric string
print("".join(b))

# Write a Python program to get the 4th element and 4th element from last of a tuple.
print(tuplex)
print("The fourth element from starting is:",tuplex[3],"The 4th element from the last is:",tuplex[-4])

# Write a Python program to create the colon of a tuple.
# colon means copy of tuple
from copy import deepcopy
d=["hi",2.8,5,[],(),True]
n=deepcopy(d)
n[3].append(10)
n[4]=n[4]+(5,)
print(n)
print(d)

# Write a Python program to find the repeated items of a tuple.
a=(1,2,2,2,2,2,2,9,-2)
t=len(a)
i=0
while i<t:
    if a[i] in a[i+1:]:
        print("The Element is:",a[i],":","count value will be:",a.count(a[i]))
    i+=1    

for i in range(t):
    print("The Number is:",a[i],":",a.count(a[i]))

    


