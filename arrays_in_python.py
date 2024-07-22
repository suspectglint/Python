#This program is for demonstrating the usage of array in Python programming language.

from array import *

arr = array('i',[1,2,3,4])
print(arr,type(arr),len(arr))

#arr[2] = array('i',[25]) #doesnot work

#Indexing and slicing in arrays
print(arr[0],arr[1],arr[2],arr[3],arr[-1],arr[-2],arr[0:2])
print(type(arr[0]))
print(id(arr[0]))
print(id(arr[1]))
print("Invalid Slice = ",arr[-3:1],"Length = ",len(arr[-3:1]))

#typecode and itemsize variables in array class
print("arr.typecode = ",arr.typecode,type(arr.typecode),sep=" ")
print("arr.itemsize = ",arr.itemsize,type(arr.itemsize),sep=" ")

#using dir() method mentioned in Schafer's class 
#dir() - used to print describe the methods present in class(object/class name can be given as input)
# dunder methods are also included.
print(dir(arr),"\n")
print(dir(array))







"""
#Experimenting to check the id's of stand-alone variables 
with id's of elements in array where the values are same.
c,d = 1,2
print(id(c))
print(id(d))

d = (f for f in arr)
print(d,type(d))"""

