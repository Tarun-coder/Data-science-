import random
while True:
    number=int(input("Enter the Number: "))

    number_2=random.randint(1,10)
    print("The Number generated by machine is: ",number_2)

    if number==number_2:
        print("Horray your Guess is Right")
    else:
        print("Opps!! Better Luck next time")    