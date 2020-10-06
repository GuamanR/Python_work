###1
##
##def what_day_is_it(x):
##    if x==0:
##        print("Today is Sunday")
##    elif x==1:
##        print("Today is Monday")
##    elif x==2:
##        print("Today is Tuesday")
##    elif x==3:
##        print("Today is Wednesday")
##    elif x==4:
##        print("Today is Thursday")
##    elif x==5:
##        print("Today is Friday")
##    elif x==6:
##        print("Today is Saturday")
##    else:
##        print("You have the wrong number, try again")
##        return
###2
##    
##def you_are_in_jail(day, time):
##    total=day+time
##    x=total%6
##    what_day_is_it(x)
##
##day = int(input("What day is it?"))
##time =int( input("How long will you be staying?"))
##
##you_are_in_jail(day,time)

###6
##def whats_my_grade(x):
##        if x>=75:
##            print("First")
##        elif 70<=x<75:
##            print("Upper Second")
##        elif 60<=x<70:
##            print("Second")
##        elif 50<=x<60:
##            print("Third")
##        elif 45<=x<50:
##            print("F1 Supp")
##        elif 40<=x<45:
##            print("F2",)
##        else:
##            print("F3",)
##xs=[83,75,74.9,70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]
##for i in xs:
##    whats_my_grade(i)

#This one is for the turtle chart

import turtle

xs=[48, 117, 200, 240, 160, 260, 220]

def draw_bar_chart(t, height):
        t.left(90)
        t.forward(height)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.penup()
        t.forward(10)
        t.pendown()

richie=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")


for i in xs:
        draw_bar_chart(richie, i)

wn.mainloop()
    
    
