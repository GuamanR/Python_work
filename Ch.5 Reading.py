# This chapter is about conditionals

#True and False MUST be capitalized
#These are boolian Expressions
 5==2
 # this tests if the two are equal

 x!=y   #Tests if the two are NOT equal
 x>y    #X is greater than y
 x<y    #x is less than Y
 x>=y   #x is greater than or equal to y
 x<=y   #x is less than or equal to y
 
#LOGICAL OPERATORS

 and
 or
 not        #negates a boolian value

x and False == False
False and x == False
y and x == x and y              #with the and statement, False wins
x and True == x
True and x == x
x and x == x

x or False == x
False or x == x
y or x == x or y
x or True == True
True or x == True       #seems like with the or statement, true wins
x or x == x

if x%2==0:
    print(x,"is even")
else:
    print(x,"is odd")
pass

#can use the pass staement to hold the place of code that has not been written yet :)

#if you dont want to use the else statemet, then you can just use the if and if the statement is false,
#then it goes to the next unindented line of coding

#can put functions inside of the print funciton

#CHAINED CONDITIONALS
if
elif
else

#conditionals can also be nested(try to avoid)

#The return function with or without a value assigned terminates functions
#also avoid using the not statements

not (x and y)  ==  (not x) or (not y)
not (x or y)   ==  (not x) and (not y)      #the not negates the and/or sign

#remember
float
str
int

richie.begin_fill()
richie.end_fill()
#or we can use
richie.color("red","blue")
richei.write("hello")

