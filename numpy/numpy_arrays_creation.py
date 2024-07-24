"""
This program shows the creation of numpy arrays in python using the following methods :-
-> array()
-> linspace()
-> logspace()
-> arange()
-> ones() and zeros()
"""

#import all classes, functions and variables from numpy
from numpy import *

#1. array() - creation using array
tmp = array([1,2,3,4,5])
print(tmp)
print(type(tmp))
print(tmp[0])
print(type(tmp[0]))

tmp = array([1,2,3,4,5],dtype=float)
print(tmp)
print(type(tmp))
print(tmp[0])
print(type(tmp[0]))

tmp = array(['a','b','c'])
print(tmp)
print(type(tmp))
print(tmp[0])
print(type(tmp[0]))

tmp = array(['Akbar','Babar','Chahbaz'],dtype=str)
print(tmp)
print(type(tmp))
print(tmp[0])
print(type(tmp[0]))

print(array,type(array)) #<built-in function array> <class 'builtin_function_or_method'> - explanation?

#2. linspace(start,end,n) - creation using linspace - creates equally distant members including stat and end.
a = linspace(1,20,7)
print(a,type(a))
print(a[4],type(a[4]))

a = linspace(1,20,7,dtype=int)
print(a,type(a))
print(a[4],type(a[4]))

#3. logspace(start,end,n) - creation using logspace - creates equally distant members including stat and end but on logarithmic scale.
b=logspace(1,5,9)
print(b)

#4. arange(start,end,step) - similar to range() function in python.
c =  arange(12,20,2)
print(c)

#5. zeros(n,datatype) and ones(n,datatype) - default datatype is float
zeros1 = zeros(5)
zeros2 = zeros(5,int)

ones1 = ones(5)
ones2 = ones(5,int)

print(zeros1,zeros2,type(zeros1))
print(ones1,ones2,type(ones1))