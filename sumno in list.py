# Write a Python function to sum all the numbers in a list.

# Enter the list of interger
li=[1,2,3,4,5,6,7,8,9,20,10]

def listsum():
    sum=0
    for i in list(li):
        sum=sum+i
    print("The sum of the list is",sum)
     

listsum()
