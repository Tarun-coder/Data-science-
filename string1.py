# Write a program to print every character of a string entered by user in a new line using loop.
#character=input("Enter the String: ")
#for i in character:
#      print(i)

# Write a program to find the length of the string "refrigerator" without using len function.

#ch1=input("Enter the string:")
#count_num=0
#for i in ch1:
#    count_num+=1
#print("The lenth of the String is: ",count_num)    
    
# Write a program to check if the letter 'e' is present in the word 'Umbrella'.
#b="Umbrella"
#print("e" in b)
  
 # Write a program to check if the word 'orange' is present in the "This is orange juice".
#s="This is orange juice" 
#print('orange' in s.split())

# Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is.
# For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.

#full_name=input("Enter the Full Name: ")
#c=full_name.split()
#print(c[0][0],".",c[1][0],".",c[2])

print("-----------")

name=input("Enter the Name: ")
for i in name:
    if i.isdigit():
        name=name.replace(i,"",1)
print(name)  

# Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day".
s="Hello, have a good day "
v="aeiou"
for i in s:
    if i not in v:
        s=s.replace(i,"",1)
print(s)        
        

