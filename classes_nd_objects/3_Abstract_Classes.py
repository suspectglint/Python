#This program is used to understand the abstract classes.



from abc import ABC,abstractmethod


#ABC must be inherited inorder to create a abstract class
class Animal(ABC):

    #This decorator mandates the subclasses to implement this method. 
    #Failing to do so will result in failures while creating an object.
    @abstractmethod
    def mobility(self):
        pass

class Goat(Animal):

    def __init__(self,name):
        self.name = name

    def mobility(self):
        return f"{self.name} walks on four legs."

g1=Goat("Simba")
print(g1.__dict__)
print(g1.mobility())