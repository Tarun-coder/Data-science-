# Write a Python function that takes a list and returns a new list with unique elements of the first list.

a =int(input("Enter the size of the list : " ))
li=[]
for i in range(a):
    number=int(input("Enter the Number to add into list: "))
    li.append(number)
    print("The value of the list",li)

print("The Final list is :",li)

def uniquelist(li):
    nli=[]
    for i in li:
        if i not in nli:
            nli.append(i)
            print("The unique list is :",nli)

uniquelist(li)            
                        
   
