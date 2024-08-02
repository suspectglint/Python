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