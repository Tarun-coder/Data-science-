# Write a Python program to count the number of characters (character frequency) in a string.

character=input("Enter the String : ")
a=len(character)
print("This is a lenth of the String",a)

for i in range(a):
    c=character[i]
    d=character.count(str(c))
    print(c,":",d)
    print()



# output
e : 2

w : 1

e : 2

s : 1

t : 1




