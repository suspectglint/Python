#Various datatypes used in python including strings
#This script is only for string data type

msg = 'TIANZHU'

print(msg)
print()

msg1 = """ This is a multi  
lined string """

print(msg1)
print()
# Indexing
print(msg[0])

#Slicing
print(msg[0:])
print(msg[:5])
print(msg[0:5:2])

#methods for string
print(msg.find('A'))
print(len(msg))
print(msg.replace('Z','ZZ'))

#know more about a object
print(dir(msg))

#help 
#print(help(str))

