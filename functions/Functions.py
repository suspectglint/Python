#This program contains the following things related to functions :-
#Formal & Actual Arguments
#Positional Arguments, Default Arguments, Key Word Arguments and Variable Arguments
#Lambda Functions - Anonymous Functions
#filter,map and reduce functions and their usage
#global keyword and globals[] 
#Decorators - Decorator functions, how they are built and used.
#Generators - Generator functions using yield to return generator objects
#__name__ - variable created internally by python where the value stored in it can be used to determine 
#           if the program is executed as a individual script or a module.

from functools import reduce

#Default Arguments
def fn1(a = 11,b = 23):
    return a+b
print(fn1())
print(fn1(7))
print(fn1(9,11))

#Keyword Arguments
def fn2(fname,lname,mname="Reddy"):
    return f"My Fullname is {fname} {mname} {lname}"
print(fn2(mname="Reddy",lname="Rokkam",fname="Gopi Shravan"))
print(fn2(lname="Rokkam",fname="Gopi Shravan",mname="Reddy"))
print(fn2(lname="Rokkam",fname="Gopi Shravan"))

#Variable Arguments - is able to take multiple arguments in the form of tuple
#we should have '*' in front of variable arguments variable and while accessing,
# it can be used as a normal tuple.  
def fn3(*vargs):
    print(vargs,type(vargs))

print(fn3(1,2,3,4))
print(fn3())

#Variable Keyword Arguments - is able to take multiple key word arguments in the form of dictionary
#we should have '**' in front of variable arguments variable and while accessing,
# it can be used as a normal dictionary.
def fn4(**kwargs):
    print(kwargs,type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

fn4(mname="Reddy",lname="Rokkam",fname="Gopi Shravan")
fn4(mname="Reddy",fname="Gopi Shravan")
fn4(name="Rokkam",fname="Gopi Shravan")
fn4()

#Lambda Functions
sqrt = lambda x : x*x
sqrt1 = lambda x : x*x
is_even = lambda x : x%2 == 0

#Although the logic is same, python is treating above two lambda as different and id is different.
print(id(sqrt),type(sqrt),sqrt(25))
print(id(sqrt1),type(sqrt1),sqrt1(35))

print(is_even(12))
print(is_even(1))
print(is_even(-17))
print(is_even(-16))

#filter(function,iterable) - used to filter the elements of iterable where function is used
#to filter the elements in iterable.
lst=[1,2,3,4,5,6,7,8,9,10]
even_lst=filter(is_even,lst) #returns a filter object and can be converted into list using list().
print(lst,type(even_lst))
tple=(1,2,3,4,5,6,7,8,9,10)
even_tple=filter(is_even,tple)
print(tple,list(even_tple),tuple(even_tple))

lst11=list(even_lst) #Once used list(filter object) is working, but next time it is not working.
print(lst11,type(lst11))
print(tuple(lst11))

lst12=[2,4,6,8,10]
print(lst12,type(lst12))
print(tuple(lst12))

#map(function,iterable) - used to transform the values of iterable using function argument.
lst1=[1,2,3,4,5]
sqrt_lst=map(lambda x : x*x,lst1) #returns a map object
print(sqrt_lst,type(sqrt_lst),list(sqrt_lst))
#using two iterables as arguments
lst2=[2,4,6,8,10]
lst1Xlst2=list(map(lambda x,y : x*y,lst1,lst2))
print(lst1Xlst2)

#reduce() - used to reduce a given iterable to a single value
lst1=[1,2,3,4,5,6,7,8,9,10]
red_value=reduce(lambda x,y : x+y,lst1)
print(red_value,type(red_value))

#global keyword - if we want to use the global scope variables in lower scope.
#globals() - a built-in function that returns a dictionary of all the global variables with variable name as 'key' and variable value as 'value'.
testvar=1234

def global_function():
    testvar=4321
    global_testvar=globals()['testvar']
    print("testvar = ",testvar,id(testvar))
    print("global_testvar = ",global_testvar,id(global_testvar))
    print(type(globals),"type(globals()) = ",type(globals()),type(globals()['testvar']))

print(testvar,id(testvar))
global_function()
print(testvar,id(testvar))

#Decorators - Used to return a function that performs additional transformation as required over the main function.
#Following are 3 criteria for a function to act as a decorator.
#1 - Function should take function as an argument.
#2 - It should have an inner function which does the transformation to the argument passed to .
#3 - It should return that inner function as a return value.

def double_decorator(fun1):
    def inner_function(val):
        return 2*val
    return inner_function

def triple_decorator(fun1):
    def inner_function(val):
        return 3*val
    return inner_function

def tmp_fun(val):
    return val

@triple_decorator #Decorator is mentioned using '@' after which the decorator function is used.
def tmp_fun2(val):
    return val

print(double_decorator(tmp_fun)(2)) #calling decorator directly using decorator function
print(tmp_fun2(2)) # calling decorator using function upon which @decorator is used.

#Generator - function that used yield to return a sequence of values.
#what is the real use of yield keyword? - Is it used for returning values asynchronously?
def generator_function():
    i=1
    while i<=5:
        yield i
        i+=1

t=generator_function()
print(t,type(t),list(t),type(list(t)),type(t),list(t))

#Iterating through a generator
#tnp=next(t)
#print(tnp)

#__name__ variable
if __name__ == "__main__":
    print(f"This file is executed as an individual script and value of __name__ is {__name__}")
else:
    print(f"This functions is executed as a module and value of __name__ is {__name__}")