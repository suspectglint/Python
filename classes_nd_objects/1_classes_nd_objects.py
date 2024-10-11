#This program is used to understand the classes and objects creation in python.

#Class Creation - Every class is a subclass of 'object' class.
class Student(object):
    StudentCount=279 #class variable
    def __init__(self,n='',m=0) -> None:
        self.name=n
        self.marks=m
    
    def displayStudentCount(cls):
        print(f"Total Student Count is {cls.StudentCount}")

    def talk(self):
        print(f"Hi All, My Name is '{self.name}'")
        print(f"Hi All, My Marks are '{self.marks}'")
        print(f"Total Student Count is {self.StudentCount}")

s1=Student()
s2=Student('Sravan Reddy Rokkam',96)
s1.talk()
s2.talk()
s1.displayStudentCount()
s2.displayStudentCount()

print(Student.StudentCount,s1.StudentCount,s2.StudentCount)
print(id(Student.StudentCount),id(s1.StudentCount),id(s2.StudentCount))
print(id(s1.displayStudentCount),id(s2.displayStudentCount))
print(id(s1.talk),id(s2.talk))
