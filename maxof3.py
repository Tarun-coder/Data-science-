# Write a Python function to find the Max of three numbers.
# Enter the Number

num1=input("Enter the Number 1: ")
num1=int(num1)

num2=input("Enter the Number 2: ")
num2=int(num2)

num3=input("Enter the Number 3: ")
num3=int(num3)

def find_Max(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print("The Number",num1,"is largest out of the two")
        else:
            print("The Number",num3,"is largest out of two")
    else:
        if num2>num3:
            print("The Number",num2,"is the largest out of two")
        else:
            if num1==num2==num3:
                print("All the Number are Equal")
            else:    
                print("The Number",num3,"is the largest out of two")

print()
find_Max(num1,num2,num3)        



