print("-------------------------------Even list from given list--------------------------")
# Write a Python function to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

def evenlist():
    li=[]
    even=[]
    for i in range(1,10):
        li.append(i)
        if i%2==0:
            even.append(i)
    print("The list is:",li)
    print("List of Even number are:",even)

evenlist()

print("--------------------------------unique list means(no repetetion of Element)--------------------------------------------")
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def uniqueli():
    li=[]
    nwli=[]
    for i in range(10):
        number=int(input("Enter the element: "))
        li.append(number)
    print("The sample list is:",li)
    for i in li:
        if i not in nwli:
            nwli.append(i)
    print("The Unique list will be:",nwli)           

uniqueli()
print("---------------------------------------Palindrome-----------------------------------------------")
# Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
#e.g., madam or nursesrun.

def pallindrome():
    character=input("Enter the string: ")
    if character[0:] == character[::-1]:
        print("The String is Palindrome")
    else:
        print("It is not a Palindrome")

pallindrome()     

print("-------------------------------Element in a Given range----------------------------")

# Write a Python function to check whether a number is in a given range.

def checknum():
    number=int(input("Enter the number: "))
    a=range(1,101,1)
    if number in a:
        print("Number",number, "is in the Range between 1 to 100")
    else:
        print("oops!! Number:",number," not in given Range") 

checknum()       
print("-------------------------------check for factorial-------------------------------------------")
# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

num=int(input("Enter the Number: "))

def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    print("The Factorial of Given number:",num,"is:",fac) 

factorial(num)      

print("-----------------------------Reverse a String------------------------------------")

# Write a Python program to reverse a string.

character=input("Enter the String: ")

def revstr(character):
    print("The Reverse String will be:",character[::-1])

revstr(character)

print("----------------------------Multiply all num in list--------------------------")

def mullist():
    a=int(input("Enter the size of the list: "))
    li=[]
    for i in range(a):
        nub=int(input("Enter the Element: "))
        li.append(nub)
    print("The sample list is:",li)
    mul=1
    for i in li:
        mul=mul*i
    print("The Multiplication of all the element in the list will be:",mul)
    
        
        

