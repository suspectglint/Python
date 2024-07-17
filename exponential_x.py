#This program is used to calculate the exponential value of x, given x as an input.
#We are going to calculate e^x using the series expansion of e^x
#e^x = 1 + x/1! + x^2/2! + x^3/3! + x^4/4! + .... so on

import argparse

parser = argparse.ArgumentParser(description="For accepting input x value for calculating e^x")
parser.add_argument("x",type=int,help="Please enter a non-negtive integer for x!")
parser.add_argument("iter_num",type=int,help="Please enter a positive integer for number of iterations!")
args = parser.parse_args()

try :
    assert args.x >=0
except AssertionError:
    print("Invalid value for x.Please input a non-negative value for x.")

try :
    assert args.iter_num >0
except AssertionError:
    print("Invalid value for iter_num.Please input a positive value for iter_num.")

rsum = 1
tmp = 1

for i in range(1,args.iter_num+1):
    print(f'Iteration = {i} e^x = {rsum:.4f}') #Note the usage of formatting in f-strings.
    tmp = (tmp*args.x)/i
    rsum += tmp