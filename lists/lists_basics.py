#This program is built to understand the basics of lists.
#And check the functions and methods associated with creation,manipulation of lists
import sys

r=range(1,11) #returns a range object
print(r,type(r))
l=list(r)
print(l,type(l)) #returns a list object

#delete an element/slice of list using 'del' keyword
del l[4]
print(l)
del l[3:7]
print(l)

#Aliasing and Cloning
l1=list(range(1,11))
l2=l1 #Aliasing by directly assigning former to latter
print(l1,l2,id(l1),id(l2),sys.getsizeof(l1),sys.getsizeof(l2))

l3=l1[::] #using slice to clone a list.
l4=l1[:]  #using slice to clone a list.
print(l1,l3,l4,id(l1),id(l3),id(l4))

l5=l1.copy() #using copy() method to clone a list.
print(l1,l5,id(l1),id(l5))

#Concatenation - using '+' operator
l7=[1,2,3]
l8=[4,5,6]
print(l7+l8)