#This program is built to understand the basics of tuples 
#Various ways of creation of tuples, indexing, slicing, concatenation, membership etc.
#Tuples are immutable and we generally use them if we have any scenario where we donot want the sequence to be modified.

#tuple creation
tp1=(1,2,3,4)
tp2=(1,) #If we have a single element in tuple, we should enter a comma at the end else it will be considered as int.
tp3=tuple([1,2,3,4])
tp4=tuple(range(1,5))
#[If we give elements without any braces, it will be considered as a tuple]
tp5=1,2,3,4 #same id as of tp1 so both might be reference to same object.
print(tp1,tp2,tp3,tp4,tp5,id(tp1),id(tp2),id(tp3),id(tp4),id(tp5),)

#sorted() method - returns a list, we can use reverse keyword and key attribute to change the keys of sorted function.
tp6=((1,'Simba',100),(2,'Samba',50),(3,'Sumba',300),(4,'Semba',250))
print(tp6)
print(sorted(tp6),type(sorted(tp6)))
print(sorted(tp6,reverse=True))
print(sorted(tp6,key= lambda x : x[1]))
print(sorted(tp6,key= lambda x : x[2]))