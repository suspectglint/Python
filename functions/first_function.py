#First program in functions.

import argparse

def gcd(a,b):
    """This program is used to calculate the Greatest Common Divisor(G.C.D) of given 2 numbers."""
    while b!=0:
        a=a%b
        if b>a:
            a,b=b,a
    return a

parser = argparse.ArgumentParser(description="Parser for validation of arguments")

parser.add_argument("var1",type=int,help="Please enter a postive integer.")
parser.add_argument("var2",type=int,help="Please enter a postive integer.")

cmd_args = parser.parse_args()

var1=cmd_args.var1
var2=cmd_args.var2

assert var1>0, "First argument is invalid, please enter a positive integer."
assert var2>0, "Second argument is invalid, please enter a positive integer."

x = gcd(var1,var2)
print(x)