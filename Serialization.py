# Serialization : It is a process of converting structured data sets into object so that we can store that
# into file and restored back whenever required
import pickle
print("---------------------------creating the list------------------------")

li=[2,3,4,5,6,7,8]

with open("pickle.txt","wb") as f:
pickle.dump(li,f)

del li

print(li)