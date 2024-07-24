#Standard Experiment Python File - where I want to test any basic things or random one-off cases.

a=[]
for i in range(5):
    print("Enter a number : ",end='')
    a.append(int(input()))
print(a)

"""
Output for above program : 
Enter a number :  12
Enter a number :  23
Enter a number :  45
Enter a number :  12
Enter a number :  12
[12, 23, 45, 12, 12]
"""

a=[]
for i in range(5):
    print("Enter a number : ")
    a.append(int(input()))
print(a)

"""
Output for above program :
Enter a number : 
12
Enter a number :
34
Enter a number :
56
Enter a number :
67
Enter a number :
78
[12, 34, 56, 67, 78]
"""

#The difference after input() you enter a line-break character(\n - a new line) to mark the end of input.
#Now if we have end as default, print would also use end as '\n' and we get a new line.
#But when we use end='', then a new line for marking end of input is only registered.