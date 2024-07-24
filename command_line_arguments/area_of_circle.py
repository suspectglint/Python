#to find the area of a circle and the radius is taken as an input.

import argparse
import math

#Creation of Parser
parser=argparse.ArgumentParser(description="This program is for calculating the area of a circle.")

#Addition of argument to parser
parser.add_argument("radius",type=float,help="Please enter a float value which is the radius of circle :)")

#Parse the arguments passed in command line
args=parser.parse_args()

print("The radius of circle is :",args.radius)

area = math.pi * args.radius**2

print("The area of circle is :",area)
print("The ared of circle is : {:.2f}".format(area))