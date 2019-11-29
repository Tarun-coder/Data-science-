# Write a Python function to check whether a number is perfect or not.
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
# This is followed by the perfect numbers 496 and 8128.

number=int(input("Enter the Number: "))

def Perfectno(number):
    li=[]
    sum=0
    for i in range(1,number):
     
        if number%i==0:
            print("The divisor of number",number,"is:",i)
            li.append(i)
    print(li)
    add=0
    for i in li:
        add=add+i
    print("The sum is:",add)
    if add==number and (add+number)/2==number:
        print("The number ",number,"is Perfect Number")
    else:
        print("The Number",number,"is not Perfect Number")        

Perfectno(number)        
