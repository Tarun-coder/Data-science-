# Write a Python function to print the even numbers from a given list.
a =int(input("Enter the size of the list : " ))
li=[]
for i in range(a):
    number=int(input("Enter the Number to add into list: "))
    li.append(number)
    print("The value of the list",li)

print("The Final list is :",li)

print("-------------------------Even number list from original list---------------------------")
even=[]
for i in li:
    if i%2==0:
        even.append(i)
        
print("The Even list is:",even)    
        
