#Program for understanding various control statements present in python.

#############################################################
#if statement
a=123

if a == 123:
    print("Samba is Simba") #default indentation is 4 spaces in python.

a='123'

if a != 123:
 print("Simba is Samba") #But we can use any other number of spaces other than 4 as indentation.

a=345

if a == 345 : print(f'{a} is 345') # inline statement when we have only one statement in suite(group of statements with same indentation.)

if a == 345 :
   #Using  \ to escape new line and all the strings present in three lines are concatenated together in one line.
   sample_str="""Betty some butter.\
But the Butter was Bitter Butter.\
To make the Bitter Butter Better, Betty some Better Butter."""
   print(sample_str)

#############################################################

#############################################################
#if-else statement:

num = int(input("Enter a positive integer : "))
if num %2 == 0:
   print(f'{num} is an even integer.')
else:
 print(f'{num} is an odd integer.')

#Inline with single line of code in if and else blocks
if num%2==0 : print(f'{num} is an even integer.')
else : print(f'{num} is an odd integer.') 
#############################################################

#############################################################
#if .. elif .. else statement:
if num > 0:
   print(f'{num} is a postive integer.')
elif num < 0:
   print(f'{num} is a negative integer.')
else:
   print(f'{num} is zero.')

#if .. elif .. elif (observe there is no else in the below code section.)
digit=int(input("Enter a digit : "))
if digit==1:print("ONE")
elif digit==2:print("TWO")
elif digit==3:print("THREE")
elif digit==4:print("FOUR")
elif digit==5:print("FIVE")
elif digit==6:print("SIX")
elif digit==7:print("SEVEN")
elif digit==8:print("EIGHT")
elif digit==9:print("NINE")
#############################################################