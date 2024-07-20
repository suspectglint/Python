# Python script demonstrating lists, tuples and sets
# [] for lists,() for tuples,{} for sets

#Lists

list1 = ['Telugu','Hindi','English','Maths','Science','Social']
list1[5]='Social Studies'
list2 = list()
list2.extend(list1)
list2.append('Computers')
list2.insert(7,'Physical Education')
list1.sort()
print(list1)
print(list1.index('Maths'))
list1.reverse()
print(list1)
print(list1)
print(list2)
#print(dir(list)) #for knowing regarding all the methods present in the list class
#For Loop
for i in list2:
  print(i)
print(list1.count('Maths')) 
print(list2.count('Arts'))

#Tuples

tup1 = ('Ape','Baboon','Chimpanzee')
tup2 = tuple()
tup2 = tup1
print(tup1)
print(tup2)
#print(dir(tuple))

#Sets

set1 = {'Tuscon','Creta','Verna'}
set2 = {'Verna','Accent','Santro'}
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(dir(set))


















