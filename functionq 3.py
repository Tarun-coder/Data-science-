# Write a Python function to sum all the numbers in a list.
def sumli():
    a=int(input("Enter the size of the list: "))
    li=[]
    for i in range(a):
        number=int(input("Enter the Element :"))
        li.append(number)
    print("The list is:",li)
    sum=0 
    for i in li:
        sum=sum+i
    print("Total Sum of the list Element is:",sum)

sumli()
