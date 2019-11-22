# Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

user=input("Enter the string: ")
b=len(user)
count_chr=0
count_int=0
for a in user:
    if a.isalpha():
        count_chr+=1
    else:
        count_int+=1
    
print("The Total lenth of String is:",b)
print("The number of Letter is: ",count_chr)
print("The number of integer is:",count_int)


