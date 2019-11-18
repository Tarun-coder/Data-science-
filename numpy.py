print("----------------------------list sum---------------------------------")
a=[35,20,3,4,5,6,85,8,5,30]
add=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
mul=a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9]
print("The Sum is :",add)
print("The Multiplication of The List Element is :",mul)

print("----------------------Random-Pattern ---------------------------------")

for r in range(1,5,1):
    for s in range(r):
        print(" ",end=" ")
    for c in range(4):
        print("*",end=" ")
    print()    
for r in range(1,5,1):
    for s in range(r):
        print(" ",end=" ")
    for c in range(4):
        print("*",end=" ")
    print()  



    