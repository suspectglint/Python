#This program is used to understand the dictionaries in python.

from collections import *

#Converting string to dictionary(via list of strings)
stra='Fname=Sravan,Lname=Rokkam,Mname=Reddy'
str1=stra.split(',') #split is a string method that returns a list of strings based on the delimiter specified.
print(str1)
lst=[]
for i in str1:
    lst.append(i.split('='))
print(lst)
dict1=dict(lst)
print(dict1)

#Dictionary definition
dict2={'Fname': 'Sravan', 'Lname': 'Rokkam', 'Mname': 'Reddy'}
print(dict2)
print(dict2==dict1)

#Converting list to dictionary using zip
l1=[1,2,3,4,5]
l2=['Billy','Heather','Adam','Matt','Anna']
z=zip(l1,l2)
print(z,type(z))
dict3=dict(z)
print(dict3)

#Methods of dictionary
print(dict3.get(3))
print(5 in dict3)
print(8 in dict3)
dict3.update(dict2)
print(dict3)
print(dict2)
dict4=dict3.copy() #copy() - creates a different object.
print(dict3,id(dict3))
print(dict4,id(dict4))
dict3.pop(5) #pop() - used to delete given key-value pair from dictionary which takes key as an argument.
print(dict3,id(dict3))
print(dict4,id(dict4))
#fromkeys() - takes a sequence & a default value and returns a dictionary with values of sequence as keys and all keys are set to same value given in argument.
dict5=dict.fromkeys(list(range(1,11)),0) 
dict6=dict.fromkeys(tuple(range(1,11)),0)
print(dict5,dict6)

#items(),keys() and values()
#dict.items() and dict.values() - id of both these objects are same, why?
print(dict6.items(),type(dict6.items()),id(dict6.items()))
print(dict6.keys(),type(dict6.keys()),id(dict6.keys()))
print(dict6.values(),type(dict6.values()),id(dict6.values()))
a=dict6.items()
for i in a:
    print(i,i[0],i[1],type(a))

#Sorting dictionary using sorted() function and lambda functions.
dict7=dict3.copy()
print(dict7,sorted(dict7.items(),key = lambda x : str(x[0])))
print(dict7,sorted(dict7.items(),key = lambda x : str(x[1])))

#OrderedDict()
#Insertion order is preserved in OrderedDict
d1=OrderedDict()
d1['Name']='Sravan Reddy Rokkam'
d1['Age']=25
d1['Occupation']='Software Engineer'
print(d1,dict(d1))
d2=OrderedDict()
d2['Name']='Sravan Reddy Rokkam'
d2['Occupation']='Software Engineer'
d2['Age']=25
print(d2,dict(d2))
print(d1==d2,dict(d1)==dict(d2)) #False True


d1={'a':1,'b':2}
d2={'b':2,'a':1}
print(d1,d2,id(d1),id(d2),d1==d2) #comparison returns True

#defaultdict()
dd=defaultdict(int) #when we give int as an argument, the default value for any key is returned as 0.
dd[1]=234
print(dd[0],dd[1])