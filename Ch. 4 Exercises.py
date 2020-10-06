#1

import turtle

def draw_square(t,size):
    t.pendown()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.penup()
    t.forward(size*2)
richie=turtle.Turtle()
richie.color("hotpink")
wn=turtle.Screen()
wn.bgcolor("lightgreen")
richie.pensize(3)
for i in range(5):
    draw_square(richie,20)
wn.mainloop()

#2

import turtle

def increasing_square(t,size):
    t.pendown()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.penup()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(180)

richie=turtle.Turtle()
richie.color("hotpink")
wn=turtle.Screen()
wn.bgcolor("lightgreen")
richie.pensize(3)

for i in range(5):
    increasing_square(richie,(i+1)*20)
wn.mainloop()


#3/6
#this program will make any regular polygon for ya :)

import turtle
def draw_poly(t, n, sz):
    angle=(n-2)*180/n
    angle=180-angle
    for i in range(n):
        t.forward(sz)
        t.left(angle)
richie=turtle.Turtle()
richie.color("hotpink")
wn=turtle.Screen()
wn.bgcolor("lightgreen")
richie.pensize(3)

def draw_equitriangle(t,sz):
    draw_poly(t,3,sz)

draw_equitriangle(richie,50)
#draw_poly(richie,8,50)
wn.mainloop()


#4

import turtle

def draw_square_thingy(t,sz,i):
    t.left(18)
    t.forward(sz/2)
    t.left(90)
    t.forward(sz/2)
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz/2)
    t.left(90)
    t.forward(sz)
    t.left(180)
    t.forward(sz/2)

wn=turtle.Screen()
richie=turtle.Turtle()
wn.bgcolor("lightgreen")
richie.color("blue")
for i in range(10):
    draw_square_thingy(richie,200,i)

wn.mainloop()
    
    
#5

import turtle

def square_loopy(t,sz,angle):
    size=sz
    for i in range(99):
        t.right(angle)
        t.forward(size)
        size=size+3
richie=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")
richie.color("blue")
richie.speed(25)
richie.pensize(2)
square_loopy(richie,3,89)
wn.mainloop()

#7

def sum_to(n):
    blah=sum (range(n+1))
    return (blah)

sum_to(10)

#8
 def area_of_circle(r):
     a=3.14159*r**2
     return(a)

#9/10
import turtle
def make_star(t,sz):
    t.forward(sz)
    t.right(144)
    t.forward(sz)
    t.right(144)
    t.forward(sz)
    t.right(144)
    t.forward(sz)
    t.right(144)
    t.forward(sz)
    t.right(144)

richie=turtle.Turtle()
wn=turtle.Screen()
richie.color("hotpink")
wn.bgcolor("lightgreen")
richie.pensize(3)

for i in range(5):
    make_star(richie,100)
    #richie.penup()
    richie.forward(350)
    richie.right(144)
    richie.pendown()

wn.mainloop()

    

