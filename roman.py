# Write a Python class to convert a roman numeral to an integer.

integer={1000:"M",500:"D",1:"I",100:"C",50:"L",10:"X",5:"V"}

num=int(input("Enter the Number to find Roman Form : "))

if num<0 and num:
    print("oops!...Invalid Number")
else:
    print("The Roman Form of {} will be Displayed below ".format(num))    

if num in integer.keys():
    print("The Roman form of Number {} is : {} ".format(num,integer[num]))
    