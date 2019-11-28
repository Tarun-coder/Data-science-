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
            sum=sum+i
            li.append(i)
    print(sum)
    if sum==number and (sum+number)/2==0:
        print("It is Perfect number")
    else:
        print("It is not Perfect number")    


    print(li)
    add=0
    for i in li:
        add=add+i
    print("The sum is:",add)
    if add==number and (add+number)/2==number:
        print("The number is Perfect Number",number)
    else:
        print("The Number",number,"is not Perfect Number")        

Perfectno(number)        
