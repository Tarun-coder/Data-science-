# Take inputs from user to make a list.
size=int(input("Enter the Size of the list : "))
li=[]
for x in range(size):
    element=int(input("Enter the Element: "))
    li.append(element)
print("The list will be:",li)
print("--------------------------Input from User to Check Number in list if Found Delete it------")
# Again take one input from user and search it in the list and delete that element, if found.
number=int(input("Enter the Element: "))
for x in range(size):
    if number in li:
        li.remove(number)
          
print(li)    







