#This program is used to understand the class methods and static methods in python.

class Employee:
    emp_raise=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    @classmethod
    def emp_from_string(cls,sting):
        first,last,pay=sting.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1=Employee('Sravan','Reddy',50000)
print(emp1.first,emp1.last,emp1.pay)

emp2=Employee.emp_from_string('Ganga-Ram-60000')

import datetime

day = datetime.date(2025,9,28)

print(Employee.is_weekday(day))
print(emp1.__dict__)
print(emp2.__dict__)
print(type(Employee),type(emp1),type(emp2))