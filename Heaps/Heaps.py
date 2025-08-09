import heapq

#Creation of Heap using heapify() function.
l1=[2,54,1,32,78,12,7,10]
print(l1,type(l1))
heapq.heapify(l1)
print(l1,type(l1))

#Popping elements using heappop() function.
r=heapq.heappop(l1)
print("Popped Element = ",r)
print("Heap = ",l1)

#Pushing elements using heappush() function.
heapq.heappush(l1,23)
print("Heap = ",l1)

#Pusing and Popping elements using heappushpop() function
r=heapq.heappushpop(l1,71)
print("Popped Element = ",r)
print("Heap = ",l1)

#Popping and pushing elements using heapreplace() function
r=heapq.heapreplace(l1,98)
print("Popped Element = ",r)
print("Heap = ",l1)

#Merge multiple sorted inputs into a single sorted output using merge() function
#The return type of this function is a generator.
print(heapq.merge([1,12],[3,7,9],[4,5],[6]))
output=[]
for i in heapq.merge([1,12],[3,7,9],[4,5],[6]):
    output.append(i)
print("Merged Output = ",output)

#Printing n smallest elements in heap using nsmallest() function
print("5 smallest elements in ",l1," are ",heapq.nsmallest(5,l1))

#Printing n largest elements in heap using nlargest() function
print("5 largest elements in ",l1," are ",heapq.nlargest(5,l1))