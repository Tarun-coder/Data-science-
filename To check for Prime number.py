# Write a python program to check whether given number is prime
# To Take value from the user

number=input("Enter the Number between 1 to 10: ")
number=int(number)

print("---------------------To check for Prime Number-------------------------------")
prime_number=[2,3,5,7,9]

if number in prime_number:
    print("The number",number,"is Prime number")
else:
    print("oops!! Its not a Prime Number")

