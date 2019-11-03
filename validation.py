import random
# It is resposible to check the validation
a=163
a=chr(a)
print(a)
username=input("Enter the username:")
pswd=input("Enter the Password:")

if username=="Tarun":
    if pswd=="1234":
        print("Welcome",username)
    else:
        print("oops!!...invalid Password")
else:
    print("oops!!...invalid Username")

for i in range(6):
    number=random.randint(65,256)
    print(number,end=" ")
    number=chr(number)
    print(number,end =" ")

        
    


    


