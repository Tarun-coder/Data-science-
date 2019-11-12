# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
num1=input("Enter the start value : ")
num1=int(num1)

num2=input("Enter the End value : ")
num2=int(num2)
def squarelist(num1,num2):
    square=[]
    for i in range(1,31):
        number=i**2
        print("The Number is :",number)
        square.append(number)
        print("The list Element are : ",square)

squarelist(num1,num2)