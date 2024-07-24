#This program describes the usage of the following keywords:-
#pass
#break
#return
#assert
#continue

import argparse

#pass - do nothing, when you want to do nothing for some scenarios or for the sake of making it syntactically correct.
print("*********************")
for i in range(10):
    if i%2!=0:
        pass
    else:
        print(i)
print("*********************")

#break - break out of loop(for,while ..) and execute the statement next to loop.
#Important to remember - break can be used only within a loop.
print("*********************")
for i in range(1,10):
    if i==7:
        break
    else:
        print(i)
print("*********************")

#continue - skip the current execution and start from the next iteration.
#Important to remember - continue can be used only within a loop.
print("*********************")
for i in range(10):
    if i%2==0:
        continue
    else:
        print(i)
print("*********************")


#assert - assert statement to check if a expression is fulfilled or not.
#Syntax = assert condition, "message"
print("*********************")
parser =  argparse.ArgumentParser(description="To test the functionality of assert keyword.")
parser.add_argument("num1",type=int,help="Enter an integer greater than 5 : ")
parser.add_argument("num2",type=int,help="Enter an integer greater than 1st argument : ")
args = parser.parse_args()
#assert args.num2 > args.num1, "You have entered incorrect arguments." -- Commented for the below try and except execution to work.
print(type(args))
print("*********************")

#assert using try and except
print("*********************")
try:
    assert args.num1 > args.num2
except AssertionError:
    print("Incorrect Arguments are passed to the script.")
print("*********************")
