a=input("Enter the string: ")

li=[]
for i in a:
    li.append(str(i))

print("list is",li)     
count_num=0
for i in a:
    if i.isdigit():
        count_num=count_num+1
    
print("The Number in string are:",count_num)

for i in range(count_num):
    for i in li:
        if i.isdigit():
            li.remove(i) 
        else:
            pass

print("".join(li))


