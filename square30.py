# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def squarelist():
    sqrli=[]
    for i in range(1,31):
        num=i**2
        sqrli.append(num)
    print(sqrli)

squarelist()       

