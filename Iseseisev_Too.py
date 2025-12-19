import turtle
t = turtle.Turtle()
#t.hideturtle()
t.speed(0)

a = 200
b = 90
c = 60


for i in range(4):
    t.fd(a)
    t.right(b)            

t.pencolor("green")
t.left(c)
t.fd(a)
t.right(c*2)
t.fd(a)
t.penup()
t.right(c/2)
t.fd(a)
t.right(b)
t.fd(a/4)
t.pencolor("red")
t.pendown()
t.right(b)

for j in range(3):
    t.fd(a/2)
    t.left(b)

#for x in range(75):
 #   for z in range(2):
  #      t.fd(a)
   #     t.left(b)
    #t.penup()
    #t.right(45)
    #t.fd(a/20)
    #t.left(10)
    #t.pendown()


t.done()