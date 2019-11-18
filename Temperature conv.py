# (cx 9/5)+32 = f

# If we want to Print the value from farenheit to celsius
print("Enter the Converter")
Converter=input("Enter the Converter:  ")
print("The Converter Selected is : ",Converter)
if Converter=="cels to Far":
    celscius=int(input("Enter the Temperature in celscius :  "))
    farenheit=(celscius*9/5)+32
    print("The Value in Farenheit is {}F:".format(farenheit))
else:
    farenheit=int(input("Enter the Temperature in Farenheit :  "))
    celscius=5*(farenheit-32/9)*5/9 
    print("The Value in the Celscius is :{}C  ".format(celscius))



