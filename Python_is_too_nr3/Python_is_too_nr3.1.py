# 3.1

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))


fail.close()

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

print(vastuvõetud[aasta-2011])