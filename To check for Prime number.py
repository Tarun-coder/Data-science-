# Write a python program to check whether given number is prime
# To Take value from the user

number=input("Enter the Number between 1 and 10: ")
number=int(number)
if number>0 and number<10:
    pass
else:
    print("Please Insert a Valid number between 1 and 10")
    exit()


print("---------------------To check for Prime Number-------------------------------")
prime_number=[2,3,5,7,9]

if number in prime_number:
    print("The number",number,"is Prime number")
else:
    print("oops!! Its not a Prime Number")

# wrong input result
Enter the Number between 1 and 10: 15
Please Insert a Valid number between 1 and 10

# output with specified limit
Enter the Number between 1 and 10: 5
--------------------To check for Prime Number-------------------------------
The number 5 is Prime number

# output when number is not Prime
Enter the Number between 1 and 10: 4
---------------------To check for Prime Number-------------------------------
oops!! Its not a Prime Number
