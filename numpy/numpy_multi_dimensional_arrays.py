#In this program, we look at various attributes of a numpy array.
#And also look at how we define multi-dimensional arrays and various methods/functions associated with it.

from numpy import *

##Various attributes of numpy arrays - for example here we are considering 1D array.
arr1 = arange(10)
print(arr1,type(arr1))
print(f"Dimension of arr1 = {arr1.ndim}")
print(f"Shape of arr1 = {arr1.shape}",type(arr1.shape))
print(f"Size of arr1 = {arr1.size}")
print(f"Itemsize of arr1 = {arr1.itemsize}")
print(f"Datatype of arr1 = {arr1.dtype}")
print(f"Number of bytes in arr1 = {arr1.nbytes}")

#array.reshape() - method to convert 1D arrays to 2D arrays or changing the shape of 2D arrays.
arr2=arange(1,7)
print(f"Input array = {arr2} and shape = {arr2.shape}")
arr3=arr2.reshape(2,3)
print(f"Reshaped array = {arr3} and shape = {arr3.shape}")
print(f"Input array = {arr2} and shape = {arr2.shape}")
#Checking the attributes of a 2D array for example.
print(f"Dimension of arr3 = {arr3.ndim} and type = {type(arr3.ndim)}")
print(f"Shape of arr3 = {arr3.shape}",type(arr3.shape))
print(f"Size of arr3 = {arr3.size}")
print(f"Itemsize of arr3 = {arr3.itemsize}")
print(f"Datatype of arr3 = {arr3.dtype}")
print(f"Number of bytes in arr3 = {arr3.nbytes}")

#array.flatten() - method to convert given nD array into a 1D array of elements.
arr4=array([[1,2,3],[4,5,6]],int)
print(f"Input array = {arr4} and shape = {arr4.shape}")
arr5=arr4.flatten()
print(f"Flattened array = {arr5} and shape = {arr5.shape}")

##Creation of multi-dimensional arrays using various functions like following :-
#array(),ones(),zeros(),eye() 

#create using array()
arr6=array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]],int)
print(f'Multi-D array using array() = {arr6} and Dimension = {arr6.ndim} and Size = {arr6.size}')

#create using ones((r,c),dtype) and zeros((r,c),dtype) where r-rows,c-columns and dtype-datatype
#default datatype is float
arr7=ones((3,3))
print(f"Multi-D array using ones() = {arr7} Dimension = {arr7.ndim} and Size = {arr7.size}")
arr8=zeros((4,4),int)
print(f"Multi-D array using zeros() = {arr8} Dimension = {arr8.ndim} and Size = {arr8.size}")

#create using eye(n,dataype) - creates a (n,n) shape array with all diagonal elements as 1 and 
#remaining elements are zeros. Similar to identity matrix.
arr9=eye(3,dtype='int')
print(f"Multi-D array using eye() = {arr9} Dimension = {arr9.ndim} and Size = {arr9.size}")

#reshape(array,(n,r,c)) - function to reshape the multi-dimensional arrays
#where r-rows,c-columns and n-when we want to create 3-D arrays and is mentioned when we need 3-D arrays.
arr10=array([[1,2,3],[4,5,6]])
print(f"Before : Array = {arr10} and Shape = {arr10.shape}")
arr10=reshape(arr10,(3,2))
print(f"After reshape() : Array = {arr10} and Size = {arr10.shape}")

#Creating 3-D array from 1-D array using reshape() function
arr11=arange(1,13)
print(f"1-D : Array = {arr11} and Shape = {arr11.shape}")
arr12=reshape(arr11,(2,3,2))
print(f"3-D using reshape() : Array = {arr12} and Size = {arr12.shape}")

##Indexing and Slicing in multi-dimensional arrays
arr6=array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]],int)
#Indexing
print(f"Complete array = {arr6}")
print(f"Indexed 2-D array = {arr6[0]}")
print(f"Indexed 1-D array = {arr6[0][0]}")
print(f"Indexed 1 element = {arr6[0][0][0]}")
#Slicing
print(f"Complete Array = {arr6[:,:,:]}")
print(f"Sliced 2-D Array = {arr6[0,:,:]}")
print(f"Sliced 1-D Array = {arr6[0,0,:]}")
print(f"Random Slice = {arr6[0:2,0:2,0:2]}")