#This program demonstrates the usage of various mathematical operations using numpy.

from numpy import *

x = array([1,2,3,4,5],int)
y = array([11,12,13,14,15],int)

print(f"x = {x}")
print(f"y = {y}")

#Vectorized Operations - operations in which entire array(vector) is processed just like a variable
z = x + y
print(f"z = {z}")

z = y - x
print(f"z = {z}")

z = x * y
print(f"z = {z}")

#Some of the various mathematical functions present in numpy.
#print(f"Sum of x and y = {x+y}")
#Basic mathematical operations like sum,prod,min,max
print(f"Sum of all values in x = {sum(x)}")
print(f"Product of all values in x = {prod(x)}")
print(f"Maximum value present in x = {max(x)}")
print(f"Minimum value present in x = {min(x)}")

#Trigonometrical functions - we have everything sin,cos,tan,arcsin,arcos,arctan ..
print(f"Sine of x = {sin(x)}")
print(f"Cosine of x = {cos(x)}")
print(f"Tangent of x = {tan(x)}")

#Aggregations/Summary/Statistical functions describing the various properties of array.
print(f"Mean/Average of all values present in y = {mean(y)}")
print(f"Median of all values present in y = {median(y)}")
print(f"Covariance of x = {cov(x)}")
print(f"Standard Deviation of x = {std(x)}")

#Comparison operators in numpy arrays >,<,>=,<=,== ..etc
print(f"Comparison x>y = {x>y}", type(x>y))
print(f"Comparison x<y = {x<y}")
print(f"Comparison x==y = {x==y}")
print(f"Comparison x==0 = {x==0}")
print(f"Comparison x>3 = {x>3}")

a = x > y
b = x < y

# any, all functions
print(any(a),type(any(a)),type(any))
print(all(b),type(all(a)),type(all))


#Logical Operators - logical_and,logical_or,logical_not,logical_xor
p = logical_and(x>=3,y>=13)
print(p,type(p))
q = logical_not(x)
print(q,type(q))
r = logical_not(q)
print(r,type(r))

#where function - somewhat similar to ternary operator
d = where((x+y)%3==0,x,y)
print(f"d = {d}")

#nonzero function - returns the indices of non-zero elements present in array.
f = array([0,1,7,8,0,4],int)
print(f)
g = nonzero(f)
print(g)

#Aliasing,Viewing,Copying

#Aliasing
print("Aliasing")
g = array([1,2,3,4,5],int)
h = g
print(f"Before g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
h[0]=99
print(f"After g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
print("Individual ids :")
print(id(g[0]),id(g[1]),id(g[2]),id(g[3]),id(g[4]))
print(id(h[0]),id(h[1]),id(h[2]),id(h[3]),id(h[4]))

#Viewing
print("Viewing/Shallow Copying")
g = array([1,2,3,4,5],int)
h = g.view()
print(f"Before g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
h[0]=99
print(f"After g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
print("Individual ids :")
print(id(g[0]),id(g[1]),id(g[2]),id(g[3]),id(g[4]))
print(id(h[0]),id(h[1]),id(h[2]),id(h[3]),id(h[4]))

#Copying
print("Copying/Deep Copying")
g = array([1,2,3,4,5],int)
h = g.copy()
print(f"Before g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
h[0]=99
print(f"After g = {g} and h = {h}, id(g) = {id(g)} and id(h) = {id(h)}")
print("Individual ids :")
print(id(g[0]),id(g[1]),id(g[2]),id(g[3]),id(g[4]))
print(id(h[0]),id(h[1]),id(h[2]),id(h[3]),id(h[4]))

#Slicing and Indexing
samp_arr=array([1,2,3,4,5],int)
print(samp_arr[:])
print(samp_arr[2:])
print(samp_arr[:3])
print(samp_arr[-2:-4:-1])

print(samp_arr[0],samp_arr[1],samp_arr[2])
print(samp_arr[-4],samp_arr[-1],samp_arr[-2])