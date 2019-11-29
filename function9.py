# Print multiplication table of 12 using recursion.

num=int(input("Enter the Number:"))
def mult12(num,i=1):
    if i<11:
        mul=num*i
        print(num,"x",i,"=",mul)
        i+=1
        mult12(num,i)
        
mult12(num)        