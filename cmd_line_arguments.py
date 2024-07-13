#This program accepts command line arguments and processes them to give result.
#This program also displays the usage of argparse module and various functions present in it.

import argparse

parser = argparse.ArgumentParser(description='To check the usage of argparse module.')
parser.add_argument("input1",type=int, help = "Please enter an integer number :)")
parser.add_argument("input2",type=str, help = 'Please enter an integer number :)')

args = parser.parse_args()
print(args,type(args))

print(args.input1,type(args.input1))
print(args.input2,type(args.input2))