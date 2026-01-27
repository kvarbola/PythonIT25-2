# Harjutus 11
# Kauri Varbola

import turtle
import random
turtle.speed(0)

def pikim_sona(list):
   pikimArv = 0
   PikimNimi = ""
   for i in list:
       if len(i) > pikimArv:
           pikimArv = len(i)
           PikimNimi = i
   return PikimNimi
    
def kolm_pikimat_sona(list):
        if len(list) > 2:
            list.sort(key = len, reverse = True)
            return list[0:3]


def viisnurk(k):
    for i in range(5):
        turtle.pendown()
        turtle.fd(k)
        turtle.rt(144)

def ring(r):
    turtle.circle(r)

def ruut(k):
    for i in range(4):
        turtle.fd(k)
        turtle.lt(90)

def suvaline(k):
    suv = random.randint(1,3)
    if suv == 1:
        viisnurk(k)
    elif suv == 2:
        ring(k)
    elif suv == 3:
        ruut(k)
    

nimed = ["Joosep", "Joonas", "Frederick", "Sergei", "Kauri", "Maria",]
print(pikim_sona(nimed))
print(kolm_pikimat_sona(nimed))

suvaline(100)

turtle.done()