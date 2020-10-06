### Functions
##
### This is how they should be set up for
##
##def NAME( parameters) :
##    statements
##


import turtle

def draw_square(t,sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.right(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")
alex=turtle.Turtle()
draw_square(alex,50)
wn.mainloop()

##heres a new fun example that has the functioninside of a for loop

import turtle

def draw_multicolor_square(t,sz):
    "make t draw square of size sz"
    for i in ["red","blue","green","purple"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
wn=turtle.Screen()
wn.bgcolor("lightblue")     
tess=turtle.Turtle()
tess.pensize(3)                                     ####

size=20
for i in range(20):
    draw_multicolor_square(tess,size)
    size=size+10
    tess.forward(10)
    tess.right(18)
wn.mainloop()


abs()       #absolute value of a number
pow(x,y)  #x to the y power
max(list)       #gives max of the list
#void funtions return useful things whereas fruitful functions return useful values

# ina  function remember to use
return x
#in order to get a value back from the function

#variables inside functions stay only inside functions and cannot be called outside of function
# make sure if you use turtles in a function to return t or w so that it becomes part of the screen 




        
    
