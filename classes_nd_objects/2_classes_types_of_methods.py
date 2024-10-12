#In this program, we implement instance methods, class methods and static methods.
#And also the instance variables, class variables.
#name mangling.

class Student(object):
    StudentCount=279 #class variable
    def __init__(self,n='',m=0) -> None:
        self.name=n
        self.marks=m
        self.__stipend=30300 #private variable
    
    @staticmethod
    def statmethod(x,y):
        print(f"Static Locals = {locals()}")
        return x*y

    @classmethod
    def classmethod(classee):
        print(f"Total Student Count is {classee.StudentCount}")
        return classee.StudentCount

    def displayStudentCount(cls):
        print(f"Total Student Count is {cls.StudentCount}")

    def talk(self):
        print(f"Hi All, My Name is '{self.name}'")
        print(f"Hi All, My Marks are '{self.marks}'")
        print(f"Total Student Count is {self.StudentCount}")

s1 = Student("Jackson",97)        

print(Student.statmethod(23,45))
print(Student.classmethod())
print(s1.statmethod(12,34))
print(s1.classmethod())

#Name mangling - <object>._<class>__<variable> This is the syntax used to access private variables called as name mangling.
print(s1._Student__stipend)

print(globals(),'\n','\n')
print(locals())

print('\n','\n',dir(Student),'\n','\n')
print(dir(s1))
print()
print()
print(dir(dir))
print()
print()
print(dir(globals))
print()
print()
print(dir(locals))
print()
print(dir())