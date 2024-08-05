#This program is built to insert a string at a given position in input string.

import sys
import argparse

parser=argparse.ArgumentParser(description="This program is for inserting a given input string at a given input position.")
parser.add_argument("str1",type=str,help="Please give string as an input!!!")
parser.add_argument("str2",type=str,help="Please give string as an input!!!")
parser.add_argument("int1",type=int,help="Please give integer as an input!!!")

args=parser.parse_args()

main_string=args.str1
insert_string=args.str2
position=args.int1

print(f"Main String = '{main_string}', Insert String = '{insert_string}' and Position = '{position}'")
result_str=""

result_str+=main_string[:position+1]
result_str+=insert_string
result_str+=main_string[position+1:]

print(f"Final result string is : {result_str}")