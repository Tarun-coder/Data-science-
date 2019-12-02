# Create a Cricle class and intialize it with radius.
#  Make two methods getArea and getCircumference inside this class.

class Circle:
    PI = 3.14

    def __init__(self,radius):
        self.radius=radius

    def getArea(self,PI=3.14):
        print("The Area of the Circle is:",PI*self.radius**2)

    def getCircumference(self,PI=3.14):
        print("The Circumference of the Circle is:",2*PI*self.radius)

circle_1=Circle(int(input("Enter the Radius of Circle: ")))
print("-------------------------------Area of the Circle---------------")
circle_1.getArea()
print("------------------Circumference of the Circle------------------------")
circle_1.getCircumference()

        