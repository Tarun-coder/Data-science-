# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
number=input("Enter the Number : ")
number=int(number)
if number<0:
    print(" oops!! Invalid Number ... Hint:Enter the Non-negative Number")
    exit()


def fac(number):
    factorial=1
    for i in range(1,number+1):
        factorial = factorial*i
    print("The Factorial of",number,"is :",factorial)

fac(number)
