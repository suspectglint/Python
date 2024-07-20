(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list1 = [1,2,3,4,5]
>>> 
>>> 
>>> list2 = [i*i*i for i in list1]
>>> 
>>> 
>>> list2
[1, 8, 27, 64, 125]
>>> 
>>> 
>>> 
>>> list3 = [i*i for i in list1 if i%2==0]
>>> 
>>> 
>>> list3
[4, 16]
>>> 
>>> 
>>> list4 = [i for i in list1 if i==i]
>>> 
>>> 
>>> list4
[1, 2, 3, 4, 5]
>>> 
>>> 
>>> tuple1 = ()
>>> 
>>> tuple1 = (1,2,3,4)
>>> 
>>> 
>>> 
>>> tuple2 = (i for i in tuple1)
>>> 
>>> 
>>> tuple2
<generator object <genexpr> at 0x7f758ed13ed0>
>>> 
>>> 
>>> 
>>> 
>>> set1 = {1,2,3,4}
>>> 
>>> 
>>> set2 = {i for i in set1}
>>> 
>>> 
>>> set2
{1, 2, 3, 4}
>>> 
>>> 
>>> type(2)
<class 'int'>
>>> 
>>> 
>>> type(set2)
<class 'set'>
>>> 
>>> 
>>> type(tuple2)
<class 'generator'>
>>> 
>>> 
>>> print(i for i in tuple1)
<generator object <genexpr> at 0x7f758d7be3d0>
>>> 
>>> 
>>> keys1={1,2,3}
>>> 
>>> values1={"Sravan",24,"Male"}
>>> 
>>> 
>>> dict1=merge(keys1,values1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'merge' is not defined
>>> 
>>> 
>>> dict1=join(keys1,values1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'join' is not defined
>>> 
>>> 
>>> dict1=zip(keys1,values1)
>>> 
>>> 
>>> dict1
<zip object at 0x7f758d7e62d0>
>>> 
>>> 
>>> 
>>> dict1=dict(zip(keys1,values1))
>>> 
>>> 
>>> dict1
{1: 'Sravan', 2: 24, 3: 'Male'}
>>> 
>>> 
>>> 
>>> tuple2 = set(i for i in tuple1)
>>> 
>>> 
>>> tuple2 = tuple(i for i in tuple1)
>>> 
>>> 
>>> type(tuple2)
<class 'tuple'>
>>> 
>>> 
>>> tuple2
(1, 2, 3, 4)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list10 = map(lambda n: n*n,list1)
>>> 
>>> 
>>> list10
<map object at 0x7f758d7e1350>
>>> 
>>> 
>>> python -V
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> 
>>> 
>>> list10 = map[lambda n: n*n,list1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> 
>>> 
>>> list10 = map(lambda n: n*n,list1)
>>> 
>>> 
>>> list10
<map object at 0x7f758d7e1790>
>>> 
>>> 
>>> print(list10)
<map object at 0x7f758d7e1790>
>>> 
>>> 
>>> list10 = map(lambda n: n,list1)
>>> 
>>> 
>>> list10
<map object at 0x7f758d7e16d0>
>>> 
>>> 
>>> map(lambda n: n,list1)
<map object at 0x7f758d7e1350>
>>> 
>>> 
>>> quit()
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ python -V
Python 3.7.6
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ 
(base) sandeep@sandeep-Inspiron-3537:~$ python
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> 
>>> my_list=[1,2,3,4]
>>> 
>>> 
>>> map(lambda x: x+1,my_list)
<map object at 0x7f5fba9e9090>
>>> 
>>> 
>>> values1={"Sravan",24,"Male"}
>>> 
>>> 
>>> 
>>> values1=["Sravan",24,"Male"]
>>> 
>>> 
>>> keys1=['Name','Age','Sex']
>>> 
>>> 
>>> zip(keys1,values1)
<zip object at 0x7f5fba9e55a0>
>>> 
>>> 
>>> list(zip(keys1,values1))
[('Name', 'Sravan'), ('Age', 24), ('Sex', 'Male')]
>>> 
>>> 
>>> dict(zip(keys1,values1))
{'Name': 'Sravan', 'Age': 24, 'Sex': 'Male'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dict2 = [key1:value1 for key1 in keys1 for value1 in values1]
  File "<stdin>", line 1
    dict2 = [key1:value1 for key1 in keys1 for value1 in values1]
                 ^
SyntaxError: invalid syntax
>>> 
>>> dict2 = {key1:value1 for key1 in keys1 for value1 in values1}
>>> 
>>> 
>>> dict2
{'Name': 'Male', 'Age': 'Male', 'Sex': 'Male'}
>>> 
>>> 
>>> dict2==dict1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dict1' is not defined
>>> 
>>> 
>>> dict1=dict(zip(keys1,values1))
>>> 
>>> 
>>> dict2==dict1
False
>>> 
>>> 
>>> dict2
{'Name': 'Male', 'Age': 'Male', 'Sex': 'Male'}
>>> 
>>> 
>>> id(dict2)
140049152600576
>>> 
>>> 
>>> id(dict1)
140049129554720
>>> 
>>> 
>>> 
>>> 
>>> 
>>> tp1=(1,2,3,4)
>>> 
>>> 
>>> tp1
(1, 2, 3, 4)
>>> 
>>> 
>>> type(tp1)
<class 'tuple'>
>>> 
>>> 
>>> 
>>> tp2=(n*n for n in tp1)
>>> 
>>> 
>>> tp2
<generator object <genexpr> at 0x7f5fbbf16ed0>
>>> 
>>> 
>>> for i in tp2:
...    print(i)
... 
1
4
9
16
>>> 
>>> 
>>>    print(i)
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 

