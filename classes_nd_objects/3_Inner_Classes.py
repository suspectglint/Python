#Inner Classes in Python

class Employee(object):
    def __init__(self,name,age,salary,dob):
        self.name=name
        self.age=age
        self.salary=salary
        self.dob=Employee.dob(*dob)
    class dob():
        def __init__(self,year,month,day):
            self.year=year
            self.month=month
            self.day=day
    def describe(self):
        print("**********Employee Details**********")
        print(f"Name   = {self.name}")
        print(f"Age    = {self.age}")
        print(f"Salary = {self.salary}")
        print(f"DoB    = {self.dob.year}-0{self.dob.month}-{self.dob.day}")
        print("************************************")

emp1 = Employee("Sravan Reddy Rokkam",26,2374613,[1999,3,16])
emp1.describe()
emp2_DoB = Employee.dob(*[1999,3,16])
print(emp2_DoB,dir(emp2_DoB))

#If you want to outer class method, then you would need a outer class instance.
#For this you may need to pass the outer class instance to the inner class and store it somewhere.
#Using this outer class instance variable, you can now access the outer class method.