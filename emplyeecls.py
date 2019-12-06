class Employee:

    def __init__(self,emp_name,emp_id,emp_salary,emp_department,Designation):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        self.designation=Designation


    def emp_info(self):
        print("Employee id:",self.emp_id)
        print("Employee name:",self.emp_name)
        print("Employee salary:",self.emp_salary)
        print("Employee department:",self.emp_department)
        print("Employee Designation:",self.designation)


    def Promotion(self,new_designation):
        self.emp_salary+=0.3*self.emp_salary
        self.designation=new_designation
        print(self.emp_name,"salary after Promotion is:",self.emp_salary)
        print(self.emp_name,"Designation after Promotion is:",self.designation)

emp1=Employee("Rahul",321,10000,"Engineer","jr.engineer")
emp2=Employee("jay",322,10000,"Engineer","jr.engineer")
emp3=Employee("Rhaul",323,20000,"Engineer","sr.engineer")

class Company(Employee):

    def __init__(self,name,employees):
        self.name=name
        self.employees=employees

    def company_info(self):
        print("Company Name is:",self.name)
        print("Total Employees in the Company:",len(self.employees))

    
emp=[emp1,emp2,emp3]
com1=Company("Wipro",emp)
print(id(com1))

com1.company_info()
emp1.Promotion("sr."+emp1.designation)
print("---------------------------------------------------")
com2=Company("wipro",emp)
com2.company_info()
print(id(com2))

print(chr(90))

