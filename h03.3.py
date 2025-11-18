# Ülesanne 3.7: Python Turtle kolmnurk
# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
# Iga kolmnurk on järgmisest 1,5 korda eemal
# Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal

import turtle


kylje_pikkus = 100
nurk = 120
kujundi_varv = "pink"
kordaja = 3
nihe = 1.5
turtle.speed(0)
turtle.color(kujundi_varv)


for _ in range(kordaja):
    for _ in range(kordaja):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.fd(kylje_pikkus*nihe)
    turtle.pendown()

turtle.done()