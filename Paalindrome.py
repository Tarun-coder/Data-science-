# Write a Python function that checks whether a passed string is palindrome or not. 
# Go to the editor

a=input("Enter the string :  ")
b=len(a)

if a[0:] == a[::-1]:
    print("The string is Pallindrome ",a)
else:
    print("The string is not the Pallindrome")    