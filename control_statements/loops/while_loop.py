#This program demonstartes the use of While loop in python.
#We take two numbers as an input and print all the even numbers between them.

import argparse

parser = argparse.ArgumentParser(description="CMD Line arguments where we print all the even numbers present between the range of these two numbers.")
parser.add_argument("start",type=int,help="Enter starting number of the range :)")
parser.add_argument("end",type=int,help="Enter ending number of the range :)")

num_range=parser.parse_args()

start=num_range.start
end=num_range.end

print("Start = %d and End = %d"%(start,end))

print("Start = {0} and End = {1}".format(start,end))

print(f"Start = {start} and End = {end}")


if start>end:
    print("Invalid input range")

if start%2 !=0 :
    start+=1

#while loop start
while start<=end:
    print(start)
    start+=2