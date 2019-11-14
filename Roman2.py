# Write a Python script to check if a given key already exists in a dictionary.
new={1:"one",2:"two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}
keys=[1,2,3,4,5,6,7,8,9,10]
values=["one","two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

number=int(input("Enter the Key : "))

if number in keys:
    print("This key already exist in Dictionary")
else:
    print("It is a New Key and not found in the Dictionary") 


