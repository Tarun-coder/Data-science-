# Create a Student class and initialize it with name and roll number. Make methods to :
1. #Display - It should display all informations of the student.
2. #setAge - It should assign age to student
3. #setMarks - It should assign marks to the student.

class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("All Information of",self.name,"is given below")
        print("1. Name of the Student:",self.name)
        print("2. Roll No of the Student:",self.rollno)
        print("The Age of the Student:",self.age)
        print("The Total Mark Obtained is:",self.total_mark)

    def setAge(self,age):
        self.age=age

    def setMark(self,total_mark):
        self.total_mark=total_mark

student_1=Student("Rahul",320)
student_1.setAge(15)
student_1.setMark("450 out of 525")
student_1.display() 
       


        