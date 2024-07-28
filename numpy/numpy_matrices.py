#In this program, the following are discussed :-
#1. Creation of matrix using matrix(2-D array) and matrix("semi-colon separated string.")
#2. Various functions related to matrices.
#3. Basic Arithmetic Operations of Matrices
#4. Random module in numpy
#Additionally, random numbers are also discussed.

from numpy import *

print(type(matrix)) # type(matrix) is type :)

#Creation of matrix using matrix(2-D array) and the input must be a 2-dimensional array/1-D array in case of row matrix
mat_a = matrix([[1,2,3],[4,5,6]])
mat_b = matrix([[7,8,9],[10,11,12]])
mat_c = matrix([[13,14],[15,16],[17,18]])
print(mat_a,type(mat_a)) #<class 'numpy.matrix'>
print(mat_b,type(mat_b)) #<class 'numpy.matrix'>

#Creation of matrix using semi-colon separated string.
mat_d = matrix("1 2 3; 4 5 6; 7 8 9")
print(f"Matrix created using string where rows are delimted by ';' : {mat_d}")

# The below causes an error as the input is a 3-D array.
# mat_d = matrix([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])

mat_e = matrix([1,2])
print(f"Row matrix = {mat_e}")
mat_f = matrix([[1],[2]])
print(f"Column matrix = {mat_f}")

#Various functions related to matrices

#Diagonal - Main Diagonal/Principal Diagonal(get all elements in matrix where Aij for all i=j)
mat_g=matrix("11 12 13; 14 15 16; 17 18 19")
print(f"Diagonal of mat_g is {diagonal(mat_g)} and type of diagonal(mat_g) is {type(diagonal(mat_g))}")
print(f"Diagonal of mat_a is {diagonal(mat_a)} and type of diagonal(mat_a) is {type(diagonal(mat_a))}")

#Max and Min in matrix
print(f"Minimum element in {mat_g} is {mat_g.min()}")
print(f"Maximum element in {mat_g} is {mat_g.max()}")

#Sum and Mean in matrix
print(f"Sum of all elements in {mat_g} is {mat_g.sum()}")
print(f"Mean of all elements in {mat_g} is {mat_g.mean()}")


#sort the elements in matrix row-wise or column-wise
mat_h = matrix("3 1 -2; 8 2 9; 1 -10 -7")
print(f"Sort of {mat_h} row-wise is {sort(mat_h,1,)}")
print(f"Sort of {mat_h} column-wise is {sort(mat_h,0)}")

#product of the elements in matrix row-wise or column-wise
mat_i = matrix([[1,2,3],[4,5,6]])
print(f"Product of {mat_i} row-wise is {mat_i.prod(1)} and type = {type(mat_i.prod(1))}")   #<class 'numpy.matrix'>
print(f"Product of {mat_i} column-wise is {mat_i.prod(0)} and type = {type(mat_i.prod(0))}")#<class 'numpy.matrix'>

#transpose using transpose() or getT() methods
mat_j = matrix([[1,2],[3,4],[5,6]])
print(f"Transpose of {mat_j} is {mat_j.transpose()}")
print(f"Transpose of {mat_j} is {mat_j.getT()}")


#Basic Arithmetic Operations of Matrices like +,-,*,/
print(f"Sum of {mat_a} and {mat_b} = {mat_a+mat_b}")
print(f"Difference of {mat_a} and {mat_b} = {mat_a-mat_b}")
print(f"Product of {mat_a} and {mat_c} = {mat_a*mat_c}")
print(f"Division of {mat_a} and {mat_b} = {mat_a/mat_b}")

#random numbers
print(random.rand()) #random.rand() - generates a random number of float class between 0 and 1.
print(int(100*random.rand()))
print(type(random))        #module
print(type(random.rand())) #float
print(type(random.rand))   #method