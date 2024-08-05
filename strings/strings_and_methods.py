#This program is all about strings and various methods present for string manipulation.

#Creation of strings
str1 = 'This is a sample string'
str2 = "This is a sample string"
str3 = """This is a multi-line
string with many
lines present in it."""
str4 = """This is a multi-line \
string converted to single-line string \
using "\\".\
"""

print(str1,str2,str3,str4,sep='\n')
print(id(str1),id(str2),id(str3),id(str4))
#Both str1 and st2 are having the same ids as the value of both strings is same.

#Length of string
print(f"Length of {str1} is {len(str1)}")
print(type(print))

#Indexing
print(str1[1],str1[2])
#Slicing - when we want to print the string in reverse, step-size should be negative.
print(f"Reverse order using slicing - {str1[::-1]}") 


#Changing case of strings - upper,lower,casefold,title
str5="apple"
str6="BALL"
str7="cAMEL"
print("Convert to Upper Case using str.upper() : ",str5.upper())
print("Convert to Lower Case using str.lower() : ",str6.lower())
print("Convert to Casefold Case using str.casefold() : ",str7.casefold()) #what is casefold()? diff between casefold and lower
print("Convert to Camel/Title Case using str.title() : ",str7.title())

#Checking type of characters present in string
str5="apple"
str6="BALL"
str7="cAMEL"
str8="Donkey"
str9="a1b2c3d4"
str10="1234"
print(f"String is {str5} and isalpha() is {str5.isalpha()} and isalnum() is {str5.isalnum()} and islower() is {str5.islower()} and isupper() is {str5.isupper()} and isspace() is {str5.isspace()} and isdigit() is {str5.isdigit()}")
print("")
print(f"String is {str6} and isalpha() is {str6.isalpha()} and isalnum() is {str6.isalnum()} and islower() is {str6.islower()} and isupper() is {str6.isupper()} and isspace() is {str6.isspace()} and isdigit() is {str6.isdigit()}")
print("")
print(f"String is {str7} and isalpha() is {str7.isalpha()} and isalnum() is {str7.isalnum()} and islower() is {str7.islower()} and isupper() is {str7.isupper()} and isspace() is {str7.isspace()} and isdigit() is {str7.isdigit()}")
print("")
print(f"String is {str8} and isalpha() is {str8.isalpha()} and isalnum() is {str8.isalnum()} and islower() is {str8.islower()} and isupper() is {str8.isupper()} and isspace() is {str8.isspace()} and isdigit() is {str8.isdigit()}")
print("")
print(f"String is {str9} and isalpha() is {str9.isalpha()} and isalnum() is {str9.isalnum()} and islower() is {str9.islower()} and isupper() is {str9.isupper()} and isspace() is {str9.isspace()} and isdigit() is {str9.isdigit()}")
print("")
print(f"String is {str10} and isalpha() is {str10.isalpha()} and isalnum() is {str10.isalnum()} and islower() is {str10.islower()} and isupper() is {str10.isupper()} and isspace() is {str10.isspace()} and isdigit() is {str10.isdigit()}")
print("")

#Relational Operators with string
str11="Alpha"
str12="Beta"
str13="alpha"
str14="beta"
str15="alpha"
print(f"{str11} and {str12}, str1==str2 is {str11==str12}")
print(f"{str12} and {str13}, str1>str2 is {str12>str13}")
print(f"{str13} and {str14}, str1==str2 is {str13<str14}")
print(f"{str14} and {str15}, str1!=str2 is {str14!=str15}")

#Finding a substring in a given string - find(),rfind(),index(),rindex()
str16="This is insane."
str17="simba"
print(f"find() - '{str17}' is found in '{str16}' at '{str16.find(str17)}' position.")
print(f"rfind() - '{str17}' is found in '{str16}' at '{str16.rfind(str17)}' position.")
try :
    print(f"index() - '{str17}' is found in '{str16}' at '{str16.index(str17)}' position.")
except ValueError:
    print("Value is not found in string.")
try :
    print(f"rindex() - '{str17}' is found in '{str16}' at '{str16.rindex(str17)}' position.")
except :
    print("Value is not found in string.")

#Find count of a given string/character in another string
str18='Betty bought some butter. But the butter was bitter butter.To make bitter butter\
 better, betty added better butter to bitter butter.'
str19='butter'
print(str18.count(str19))
print(str18.count('Butter'))

#Replace a given string with another value in another string. replace() - this replaces all values.
str20='Betty bought some butter. But the butter was bitter butter.To make bitter butter\
 better, betty added better butter to bitter butter.'
str21='butter'
print(str20.replace(str21,'cucumber')) #replace() returns a string with replaced values. not in-place
print(str20)

#Sorting a given string using sort() - 
#1 - Convert string to list first
#2 - Then sort list(iterable)
#3 - Then convert the list back to string
str22="BOGO - BUY ONE GET ONE ROLES IN SNOWFLAKE"
print(f"Before sort : {str22}")
lst=[i for i in str22]
lst.sort() #inplace sort when is done on a list.
str23=''.join(lst)
print(f"After sort  : {str23}")

#Membership check - using in and not in
str24="rokkam gopi shravan reddy".title()
str25="Sravan"
str26="Shravan"
if str25 in str24:
    print(f"'in' - {str25} is found in {str24}.")
else :
    print(f"'in' - {str25} is not found in {str24}.")
if str26 not in str24:
    print(f"'not in' - {str26} is not found in {str24}.")
else :
    print(f"'not in' - {str26} is found in {str24}.")

#Starting and Ending methods - startswith() and endswith()
str27="Tupac Shakur"
str28="Tupa"
str29="akur"
str30="Thakur"
print(str27.startswith(str28))
print(str27.endswith(str29))
print(str27.startswith(str30))
print(str27.endswith(str30))

#Removing spaces from strings - strip(),lstrip() and rstrip()
str31="   This is insane    "
print(f"Using strip() - {str31.strip()}.")
print(f"str = {str31}")
print(f"Using lstrip() - {str31.lstrip()}.")
print(f"str = {str31}")
print(f"Using lstrip() - {str31.rstrip()}.")
print(f"str = {str31}")

#Repitition of string using **
str32="No man can hurl me down to death against my fate."
print(str32*108)