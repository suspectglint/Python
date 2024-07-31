#This program is all about strings and various methods present for string manipulation.

#Creation of strings
str1 = 'This is a sample string'
str2 = "This is a sample string"
str3 = """ This is a multi-line
string with many
lines present in it."""
str4 = """This is a multi-line \
string converted to single-line string \
using "\\".\
"""

print(str1,str2,str3,str4,sep='\n')
print(id(str1),id(str2),id(str3),id(str4))
#Both str1 and st2 are having the same ids as the value of both strings is same.