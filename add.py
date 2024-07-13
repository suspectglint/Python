#Sample python program to add two numbers.

import sys

print(sys.argv,type(sys.argv))
print(len(sys.argv))
lst = sys.argv[1:]
for i in lst:
    print(i,type(i))