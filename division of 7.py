# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
print("------------To check number that should be both divisible of 7 and multiple of 5---")

Number=input("Enter the number between 1500 and 2700 : ")
Number=int(Number)

# To check whether number is between 1500 and 2700
if Number>=1500 and Number<=2700:
    pass
else:
    print("Invalid Number It should be between 1500 and 2700")
    exit()

print("--------------------------------------------------------")

if Number%7==0:
    print("The number is Divisible by 7")
else:
    print("Number is not divisible by 7")

if Number%5==0:
    print("The number is Multiple of 5")
else:
    print("The Number is not the Multiple of 5")
    
    



