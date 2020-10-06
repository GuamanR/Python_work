#1
for i in range(5):
    print("I like turtles")

#3
for month in ["January", "February","March", "April", "May", "June","July","August","September","October","November","December"]:
    print("One of the months of the year is",month)

#4
#Tess will be facing 45 degrees to the left of east... her original starting position

#5
#a
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(xs)
    
#b
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(xs, xs**2)

#c
total=0
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    total=total+xs
print(total)

#d
total=1
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    total=total*xs
print(total)

#6
import turtle
wn=turtle.Screen()
richie=turtle.Turtle()

for i in range(8):
    richie.forward(30)
    richie.right(45)
wn.mainloop()

# for angles the formula is 180*(nsides-2)/(nsides)
#7/8
import turtle
wn=turtle.Screen()
pirate=turtle.Turtle()
heading=0
for i in [160,-43,270,-97,-43,200,-940,17,-86]:
    pirate.left(i)
    pirate.forward(100)
    heading=heading+i
wn.mainloop()

print("The pirate's final heading is ", heading)

#11
#36degrees

import turtle
wn=turtle.Screen()
richie=turtle.Turtle()
richie.right(108)
for i in range(5):
    richie.forward(200)
    richie.left(144)
wn.mainloop()

12

import turtle
wn=turtle.Screen()
richie=turtle.Turtle()
richie.shape("turtle")
wn.bgcolor("lightgreen")
richie.color("blue")
richie.penup()
richie.stamp()
richie.speed(5)
richie.right(90)
simran=turtle.Turtle()
simran.color("blue")
simran.penup()
simran.speed(5)
simran.right(90)

for i in range(6):
    richie.forward(200)
    simran.forward(180)
    simran.pendown()
    simran.forward(-40)
    simran.penup()
    simran.forward(-320)
    simran.pendown()
    simran.forward(40)
    simran.penup()
    simran.forward(140)
    richie.stamp()
    richie.right(180)
    richie.forward(400)
    richie.stamp()
    richie.forward(-200)
    richie.right(30)
    simran.right(30)
richie.right(90)

wn.mainloop()




