numb1=int(input("Enter the 1st Number: "))
numb2=int(input("Enter the 2nd Number: "))
operation=input("Select the Operation: ")

def calculator(numb1,numb2,operation):
    if operation=="add":
        c=numb1+numb2
        print("Addition is:",c)
    elif operation=="mul":
        print("Multiplication is:",numb1*numb2)
    elif operation=="div":
        print("Division is:",numb1/numb2)
    else:
        print("Subtraction is:",numb1-numb2)

calculator(numb1,numb2,operation)      


