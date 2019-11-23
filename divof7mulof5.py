# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) 
number=int(input("Enter the Number between 1500 and 2700: " ))
if number>=1500 and number<=2700:
    pass
else:
    print("oops!! Invalid Number Please Enter number between 1500 and 2700")
    exit()

if number%7==0 and number%5==0:
    print("The Number is Divisible by 7 and multiple of 5")
    print(5,"x",number//5,"=",number)
else:
    print("Either number is not divisble by 7 or it is not multiple of 5")