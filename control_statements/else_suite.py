#This program demonstrates the usage of else suite with while loop and for loop.

#else with for loop. The below construct prints till 9 and the else part is also executed.
for i in range(1,10):
    if i == 5*5:
        break
    else:
        print(i)
else:
    print("Else Suite :)")

#print("i = ",i,"id of i = ",id(i))

#else with for loop. The below construct doesnot enter for loop and the else part is also executed.
for i in range(0):
    if i == 5*5:
        break
    else:
        print(i)
else:
    #print("i = ",i,"id of i = ",id(i))
    print("Else Suite :)")

#else with for loop. The below construct prints only till 4 and the else part is also not executed.
for i in range(1,10):
    if i == 5*1:
        break
    else:
        print(i)
else:
    print("Else Suite :)")


#else with while loop. The below construct prints till 9 and the else part is also executed.
i=1
while i <= 10 :
    if i == 5*5:
        break
    else:
        print(i)
    i+=1
else:
    print("Else Suite :)")