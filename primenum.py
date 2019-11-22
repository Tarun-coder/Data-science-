number=int(input("Enter the Number: "))

if number>1:
    for i in range(2,number):
        if number%i==0:
            print(number,"is not a Prime Number")
            print(i,"x",number//i,"=",number)
            break   
    else:
        print(number,"is a Prime number")
             
else:
    print(number,"is not a Prime Number")       

i=4
print("----------------------------------------------------")
odd=[]
for i in range(1,100):
    if i%2==0:
        continue   
    print(i)
    odd.append(i)
print(odd)

    