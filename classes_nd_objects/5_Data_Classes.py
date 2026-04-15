#This program is used to understand data classes in python.

from dataclasses import dataclass,field
import random

def token_genrtr():
    return random.randint(1,50)

#@dataclass decorator is used to define a dataclass
@dataclass
class Battlebot:
    name:str
    weapon:str
    wheels:int
    #use of field to define default values
    bot_popularity_index:int = field(default=23)
    #But this default is mostly useful when we want to define default_factory because
    #in such scenarios we can use functions to define the default values of field.
    #battle_token_number:int = field(default_factory= token_genrtr)

    ##Important
    #“default_factory is executed only in the dataclass-generated __init__()”

    #Overwriting __init__() manually
    def __init__(self, name,weapon,wheels):
        print("Hello!")
        self.name=name
        self.weapon=weapon
        self.wheels=wheels+2
        #Yes — __post_init__() will still work even if you define your own __init__() in a dataclass, but there’s an important catch:
        # Key Rule
        #If you override __init__() manually, then dataclass will NOT automatically call __post_init__().
        #You must call __post_init__() yourself explicitly.
        self.__post_init__()
        
    # __post_init__() function is used to define another dependent attributes of the object and
    # it is called after the built-in __init__() function
    def __post_init__(self):
        self.description = f"{self.name} has {self.wheels} wheels and uses '{self.weapon}' as a weapon."

b1=Battlebot("Tomb Stone","Horizontal Rotary Blade",4)
b2=Battlebot("Huge","Vertical Rotary Blade",2)
b3=Battlebot("Tomb Stone","Horizontal Rotary Blade",4)

print(b1)
print(b1.name,b1.weapon,b1.wheels)
#__str__() and __repr__() are defined here in data class by default.
print(b1.__str__())
print(b1.__repr__())
print(dir(b1))

#And also the comparison operators are defined by default in data class.
print(b1)
print(b2)
print(b3)
print(b1==b2)
print(b2==b3)
print(b1==b3)

print(b1.description)
print(b2.description)

Battlebot.bot_popularity_index=9999

print(b1.bot_popularity_index)
print(b2.bot_popularity_index)
print(b3.bot_popularity_index)

@dataclass(frozen=True)
class Book:
    name: str
    author: str
    pages: int = 356

    #Even this throws an error if we try to amend variables in __post_init__() function.
    def __post_init__(self):
        self.pages+=2

book1=Book("Introduction to Algorithms","CLRS",465)
#Assigning a value to an attribute of frozen class will throw an error.
#book1.pages=984
print(book1)