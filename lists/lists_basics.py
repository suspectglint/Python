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

#Count of a given element in a list.
t=2
l9=[1,2,3,4,5,6,7,8,9,10]
print(l9.count(t))
print(l9.count(12))

#List Comprehensions - Similar to list comprehensions we also have dictionary comprehensions and tuple comprehensions
l10=[1,2,3,4,5]
l11=[6,7,8,9,10]
l12=[i+j for i in l10 for j in l11]
print(l10)
print(l11)
print(l12)

a='SRAVAN'
b='REDDY'
c='ROKKAM'
d=[e+f+g for e in a for f in b for g in c]
print(a)
print(b)
print(c)
print(d)

l13=[1,2,43,68,90,21,49]
l14=[x for x in l13 if x%2==0]
print(l13)
print(l14)