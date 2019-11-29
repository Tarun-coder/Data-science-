# Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
 #E.g., 6 is a perfect number because 6=1+2+3].

num=int(input("Enter the Number:"))

def perfect(num):
    li=[]
    for i in range(1,num):
        if num%i==0:
            print("number is:",i)
            li.append(i)
    print(li)
    
    sum=0
    for i in li:
        sum=sum+i
    print("sum is:",sum)
    if sum==num and (sum+num)/2==num:
        print("The Number",num,"is Perfect Number")
    else:
        print("The Number",num,"is not Perfect Number")  

perfect(num)              

