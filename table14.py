# Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
number=int(input("Enter the number to Find Table of: "))
table=[]
for i in range(1,11,1):
    numb=number*i
    table.append(numb)

print("Table of Number",number,"is",table)
print("---------------table of 2---------------------")

number_1=int(input("Enter the number to Find Table of: "))
table_2=[]
for i in range(1,11,1):
    numb_1=number_1*i
    table_2.append(numb_1)

print("Table of Number",number_1,"is",table_2)  

for i in range(10):
    new=table[i]+table_2[i]
    print("14 x ",i+1,"=",new)