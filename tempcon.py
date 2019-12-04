# If we want to Print the value from farenheit to celsius
Converter=input("Enter the Converter Name:  ")
print("The Converter Selected is : ",Converter)
if Converter=="cels to far":
    celscius=int(input("Enter the Temperature in celscius :  "))
    farenheit=(celscius*9/5)+32
    print("The Value in Farenheit is {}F:".format(farenheit))
elif Converter=="far to cels":
        farenheit=int(input("Enter the Temperature in Farenheit :  "))
        celscius=5*(farenheit-32/9)*5/9 
        print("The Value in the Celscius is :{}C  ".format(celscius))
else:
    print("oops!! Please Enter the valid name of Converter from the two option:")
    print("1. From Farenheit to Celscius as: far to cels")
    print("2. From Celscius to Farenheit as: cels to far")


