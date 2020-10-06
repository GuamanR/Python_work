print("Hello, World") #here is a note
#this is how to make a note :)
print(6+4*9)

# * is multiplication and ** is exponential
#Must have print function on order for the product to show within a script
#string is a string of letters

# If confused about type just use this function type(x)
type(22)

# strings can use ', " or '''/"""
# ' is used when there are " in the displayed sentence ''' used for combination of the two and """ can span multiple lines of code :)

#When assigning variables, make sure the assigned variable comes before the equal sign

n=21
#avoid uppercase variables, also they need to either start with a letter or underscore to be considered a variable

# len(x) function returns the number of characters in a string

len("pizza")

# // is the floor operand that divides to get strictly whole numbers. will always move left

print(6/4); 

print(6//4)

print(-6//4)

# int() float() str() all will convert the things in parenthesis to what you want

#int(2.222)-> 2
#can use + for strings but will add the words together. similarily the * will multiple the string by three

# Input() allows for the user to input an item

x=input("What is your name?")
#this input will give a string value so if you are asking for a number make sure to convert it back to integer using int(x)

response = input("What is your radius?")
r = float(response)
area = 3.14159 * r**2
print("Your area is :", area)

#this works but you cannot copy and paste into shell

#Modulus operator is % and works similar to that of the division but returns the value of the remainder when divided

print(4%3)  # will give a value back equal to 1

 #x % 10 yields the right-most digit of x (in base 10). Similarly x % 100 yields the last two digits.


total_sec=int(input("How many total seconds?:"))
hours = total_sec//3600
leftover_sec = total_sec%3600
minutes = leftover_sec//60
final_sec = leftover_sec%60
print("your condensed time is:", hours , "hour(s),", minutes, "minutes, and", final_sec, "seconds")

#also ctr+3 and ctr+4 add and remove comments mass for testing of code :)

#this will be for investment amounts

t=int( input("For how many years will this be compounding?:"))
p=10000
n=12
r=.08
a=p*(1+r/n)**(n*t)
print("Your final amount of money after", t, "years is", a)

#this one will calculate time passed
t=int(input("What time is it now in military time?:"))
t=int(t/100)
w=int(input("How long do you wish to wait?:"))
w1=w%24
print("The time after your wait will be", str((w1+t)%24)+"00")

## Turtles Ch.3

import turtle
wn = turtle.Screen() #creates play space for the turtles
richie= turtle.Turtle() #makes a turle assigned to richie
richie.forward(50)
richie.left(90)
richie.forward(30)
wn.mainloop() #wait for user to close window

# here is a more complex version

#This is for all the colors
# http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
import turtle
wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.title("First Run")

john=turtle.Turtle()
john.color("lightgreen")
john.pensize(5)

john.forward(50) #or could say john.backward()
john.left(135)
john.forward(100)
john.shape("turtle")
wn.mainloop()  #Make sure to include this little bit
# also john.penup()/john.pendown() lift and lower the pen to make marks on the screen 
#Can make multiple ones but make sure to name them different names

for f in ["joe", "Zoe", "Bill"]:            #Make sure that the syntax follows []: and then indent after becayse this is a loop
    invite= "Hey "+f + ", wanna come to my party?"
    print(invite)

for i in range(4) #does all the i values up to 4 starting at 0 and not including the number 4
# variables can also be assigned to lists such as
clrs=["red","blue","green"]
for i in clrs

# here is the cool example

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
richie= turtle.Turtle()
richie.shape("turtle")
richie.color("blue")
richie.penup()
size= 20

for i in range(30):
    richie.stamp()
    size = size+3
    richie.forward(size)
    richie.right(24)
wn.mainloop()
    






