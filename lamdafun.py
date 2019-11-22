l1=[2,3,4,5,64,6,65,78,89,10]
sum=0
for i in l1:
    sum=sum+i
    
print("The sum of all the Element in the list is:",sum)

# By using while loop
sum_1=0
i=0
while i<10:
    sum_1=sum_1+l1[i]
    i+=1
print("The sum of the list is:",sum_1)

# sum of odd number
sum_2=0
for i in l1:
    if i%2==1:
        sum_2=sum_2+i

print("The sum of all odd number is",sum_2)
sum_3=0
for i in l1:
    if i%2==0:
        sum_3+=i
print("The sum of all even number is",sum_3)
    