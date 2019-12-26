from functools import reduce
n=lambda x,y:(x+y)*x*y

print(n(2,2))

a=(2,3,5,6,7,8,12,14,16)
even=list(filter(lambda n:n%2==0,a)) # to filter the values by using lamda function
print(even)
# we can use map function to perform operation on sequence eg: double all number in list 
# or we can multiply all number in list with 2.

# now we multiply the above list of even number with 2 by using Map function

double=list(map(lambda x:x*2,even))
print(double)

average=reduce(lambda x,y:x+y,even)/len(even)
print(average)

average_1=(2+6+8+12+14+16)/len(even)
print(average_1)

