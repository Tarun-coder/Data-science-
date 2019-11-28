# Write a Python function to find the Max of three numbers.
a=int(input("Enter the Number a: "))
b=int(input("Enter the Number b: "))
c=int(input("Enter the Number c: "))

def findmax(a,b,c):
    if a==b==c:
        print("All are Equal")
        exit()

    if a>b:
        if a>c:
            print("a is Greater than all")
        else:
            print("c is Greater than all")
    elif b>c:
        print("b is Greater than all")
    else:
        print("c is greater than all ")                

findmax(a,b,c)        