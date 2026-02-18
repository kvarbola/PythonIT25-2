#Harjutus 14

import turtle
turtle.speed(0)

ekraan = turtle.Screen()

def muuda_punane():
    turtle.color("red")

def muuda_roheline():
    turtle.color("green")

def muuda_sinine():
    turtle.color("blue")

def vasakKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)

def paremKlikk(x, y):
    turtle.undo()

ekraan.onscreenclick(vasakKlikk, 1) # Vasak klõps
ekraan.onscreenclick(paremKlikk, 3) # Parem klõps
ekraan.onkey(muuda_punane, "r")
ekraan.onkey(muuda_roheline, "g")
ekraan.onkey(muuda_sinine, "b")





ekraan.listen()
turtle.done()