#Standard Experiment Python File - where I want to test any basic things or random one-off cases.

import array as arr

"""
a=[]
for i in range(5):
    print("Enter a number : ",end='')
    a.append(int(input()))
print(a)


Output for above program : 
Enter a number :  12
Enter a number :  23
Enter a number :  45
Enter a number :  12
Enter a number :  12
[12, 23, 45, 12, 12]


a=[]
for i in range(5):
    print("Enter a number : ")
    a.append(int(input()))
print(a)


Output for above program :
Enter a number : 
12
Enter a number :
34
Enter a number :
56
Enter a number :
67
Enter a number :
78
[12, 34, 56, 67, 78]


#The difference after input() you enter a line-break character(\n - a new line) to mark the end of input.
#Now if we have end as default, print would also use end as '\n' and we get a new line.
#But when we use end='', then a new line for marking end of input is only registered.

print(arr.array,type(arr.array))
print(np.array,type(np.array))

Output :-
<class 'array.array'> <class 'type'>
<built-in function array> <class 'builtin_function_or_method'>
"""

#FYI - Ternary operator is present in python and it can be used as follows :
a = 15
b = 20
c = a if a>b else b # expression1 if condition else expression2
print(a,b,c)


#type of sort() in numpy matrices
from numpy import *
print(type(sort)) #class 'numpy._ArrayFunctionDispatcher'