#LIST COMPREHENSIONS
l1=[1,2,3,4,5,6]

l2=[n for n in l1]
print(l2)

l3 = [n for n in l1 if (n%2==0)]
print(l3)

l4 = [n*n for n in l1]
print(l4)

l5 = [(m,n) for m in l1 for n in l1]
print(l5)

print("\n\n\n-----------------------------------------------------------------------------")

#SET COMPREHENSIONS
s1={1,2,3,4,5,6}
print(s1)

s2={n for n in s1}
print(s2)

s2.pop()
print(s2)

l1.pop()
print(l1)


s3=zip(s1,s2)

for i in s3:
   print(i)


