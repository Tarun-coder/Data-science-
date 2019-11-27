# To check for Number Whether it is Prime or not

def prime_no(number):

    if number>1:
        for i in range(2,number):
            if number%i==0:
                print("It is a not Prime Number as it is Divisible by :",i)
                print(i,"x",number//i,"=",number)
                break
        else:
            print("The number",number,"is a Prime Number")
    else:
        print("The Number",number,"is not a Prime Number") 

try:
    number=int(input("Enter the Number: "))
    if number<0:
        print("Please Enter Non-negative Integer")
        exit()        
    prime_no(number)
except Exception as e:
    print("The Exception is:",e)
    print("Hint:Please Enter the Interger value")



