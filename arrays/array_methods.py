#This script is used to describe the usage of array methods in python.

from array import *

arr = array('L',[1,2,3,4,5])
print(arr)
print(arr.typecode,arr.itemsize)

#Append of elements using append
arr.append(6)
print(arr)

#Insert at a position
arr.insert(0,7)
print(arr)

#When we use insert using negative index, it is inserting at one position before the mentioned index in insert method.
#The key point is that insert always places the new element before the specified index, whether the index is positive or negative.
#So, when we specify a negative index, it finds the element from last and inserts an element before that index. 
arr.insert(-1,25)
print(arr)

"""
#Same applied on list.
l = [1,2,3,5]
print(l,l[-1])
l.insert(-1,6)
print(l,l[-1])"""

#pop(index) - remove an element from a given 'index', when no index is given it will remove the last value from array
arr.pop()
print(arr)
arr.pop(0)
print(arr)

"""
#Same applied on list.
l = [1,2,3,5]
l.pop(3)
print(l,l[-1])
l = [1,2,3,5]
l.pop(-1)
print(l,l[-1])"""

#remove(x) - remove the first occurence of 'x' from array.
arr.remove(3)
print(arr)

#count(x) - return the number of occurenes of 'x' from array.
print(arr.count(25))
print(arr.count(0))

#extend(x) - appends 'x' at the end of an array, 'x' can be another array or an iterable object
#Important - We can only extend with the array of same kind.
#Can it be a single element? - No, it should be a iterable
arr2=array('L',[7,8,9,10])
print(arr2)
arr.extend(arr2)
print(arr)

arr.extend([123,456,789])
print(arr)

arr.extend(range(11,20))
print(arr)


#reverse()  - reverse the order of elements in array, in-place and it doesnot create a new array.
print(arr,id(arr))
arr.reverse()
print(arr,id(arr))

l=[1,2,3,4,5]
print(l,id(l))
l.reverse()
print(l,id(l))

original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
print(original_list)  # Output: [1, 2, 3, 4, 5]


#index(x) - returns the position number of the first occurence of x in the given array else throws a ValueError if 'x' is not found in array.
print(arr.index(789),type(arr.index(789)))
try :
    print(arr.index(321),type(arr.index(321)))
except ValueError:
    print("Value is not found in array!")