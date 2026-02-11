#kilpkonna joonlaud

import turtle
turtle.speed(0)
screen = turtle.Screen()

valik = screen.numinput("Lisa pikkus!","Lisa joonlaua pikku: ",default = 31, minval = 10, maxval = 100)

nr = 20

for i in range(1, int(valik)):
    turtle.lt(90)
    turtle.fd(10+nr)
    turtle.bk(10+nr)
    turtle.rt(90)
    turtle.fd(10)
    if i % 5 == 0:
        nr = 20
    else:
        nr = 0


turtle.goto(0,0)



turtle.done()