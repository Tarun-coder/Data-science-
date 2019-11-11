# Write a Python function to check whether a number is in a given range.
number=int(input("Enter the Number: "))
def checkinrange(number):
    li = range(0,10000)
    if number in list(li):
        print("Yes..The Number is in the Range of (0 to 10000)")
    else:
        print("oops!!...The Number is out Range")

checkinrange(number)        