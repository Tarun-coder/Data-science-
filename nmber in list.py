# Write a Python function to check whether a number is in a given range.
number=int(input("Enter the Number: "))
def range(number):
    li = [0,1,2,3,4,5,6,7,8,9]
    if number in list(li):
        print("Yes..The Number is in the Range of (0 to 9)")
    else:
        print("oops!!...The Number is out Range")

range(number)        