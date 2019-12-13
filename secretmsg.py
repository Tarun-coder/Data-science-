# We can provide security to the message so that it cant be loss during the 
# transmission of message from sender to Receiver

message=input("Enter the message: ")
key=int(input("Enter the Key between(1,26): "))
li=[]
for i in message:
    a=ord(i)
    b=a+key
    c=chr(b)
    li.append(c)

print("Secret Message will be:",''.join(li))
li1=[]
n=''.join(li)
for i in n:
    g=ord(i)
    f=g-key
    h=chr(f)
    li1.append(h)
original_msg=''.join(li1)  
print("original message will be:",original_msg)  

