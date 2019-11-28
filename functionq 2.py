
print("----------------------------Multiply all num in list--------------------------")

def mullist():
    a=int(input("Enter the size of the list: "))
    li=[]
    for i in range(a):
        nub=int(input("Enter the Element: "))
        li.append(nub)
    print("The sample list is:",li)
    mul=1
    for i in li:
        mul=mul*i
    print("The Multiplication of all the element in the list will be:",mul)

mullist()    