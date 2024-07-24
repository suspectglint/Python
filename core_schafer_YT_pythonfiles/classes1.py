#This is the first Object Oriented Program in Python by me

class Employee:
    def __init__(self,fname,lname,salary):
       self.fname=fname
       self.lname=lname
       self.salary=salary
       Employee.company='HSBC'
    def getName(self):
       return self.fname+' '+self.lname
    def getSalary(self):
       return self.salary
    @classmethod
    def getOrgInfo(clrs):
       return 'Hong Kong and Shanghai Banking Corporation(HSBC)'

emp1 = Employee('Jaipal Reddy','Rokkam',90000)
emp2 = Employee('Swarajyam','Koosukuntla',80000)
emp3 = Employee('Sandeep Reddy','Rokkam',70000)
emp4 = Employee('Sravan Reddy','Rokkam',60000)

print(emp1.getName())
print(emp2.getName())
print(emp3.getName())
print(emp4.getName())

print()

print(emp1.getSalary())
print(emp2.getSalary())
print(emp3.getSalary())
print(emp4.getSalary())

print()

print(id(emp1.getSalary()))
print(id(emp2.getSalary()))
print(emp3.getSalary())
print(emp4.getSalary())

print()

print(emp1.getOrgInfo())
print(emp2.getOrgInfo())
print(emp3.getOrgInfo())
print(emp4.getOrgInfo())

print()

print(id(emp1.getOrgInfo))
print(id(emp2.getOrgInfo))
print(id(emp3.getOrgInfo))
print(id(emp4.getOrgInfo))
print(id(Employee.getOrgInfo))

print()

print(Employee.company)
print(emp1.company)
print(emp2.company)

print()

print(id(Employee.company))
print(id(emp1.company))
print(id(emp2.company))