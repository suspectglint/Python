#To check the usage of for loop in python

a=3

print(a,id(a))

nums = range(10)
print(id(nums))
print(nums[3],id(nums[3]))
print(nums,type(nums))
print(nums[9],type(nums[9]))
print(type(range(10)))

#Incorrect - range() function only accepts int as an argument. no other types are allowed.
"""charset = range(1.0,2.5,0.5)
print(charset)"""

### Print the triangle star pattern using for loop
"""
       *
      * *
     * * *
    * * * *
   * * * * *
  * * * * * *
 * * * * * * *
* * * * * * * *
"""
n=20
for i in range(1,11):
    print(' '*(n-i),end='')
    print("* "*i)
