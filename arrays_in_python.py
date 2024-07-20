#This program is for demonstrating the usage of array in Python programming language.

from array import *

arr = array('i',[1,2,3,4])
print(arr,type(arr),len(arr))

#arr[2] = array('i',[25]) #doesnot work

print(arr[0],arr[1],arr[2],arr[3],arr[-1],arr[-2],arr[0:2])
print(type(arr[0]))
print(id(arr[0]))
print(id(arr[1]))

c,d = 1,2
print(id(c))
print(id(d))

d = (f for f in arr)
print(d,type(d))