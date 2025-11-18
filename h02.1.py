#Kauri Varbola
#10.11.25

import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=400)
t.speed(0)
#sinine
t.penup()
t.goto(-110,0)
t.pendown()
t.pensize(6)
t.pencolor("blue")
t.circle(50)
#must
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(6)
t.pencolor("black")
t.circle(50)
#punane
t.penup()
t.goto(110,0)
t.pendown()
t.pensize(6)
t.pencolor("red")
t.circle(50)
#kollane
t.penup()
t.goto(-55,-55)
t.pendown()
t.pensize(6)
t.pencolor("yellow")
t.circle(50)
#roheline
t.penup()
t.goto(55,-55)
t.pendown()
t.pensize(6)
t.pencolor("green")
t.circle(50)


turtle.done()