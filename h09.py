#Kauri Varbola

#Harjutus 9.1

#for i in range(1, 21):
#    print(i)


# Harjutus 9.3

#matrix = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]

#paaris = []
#paaritud = []

#for arv in matrix:
#    if arv % 2 == 0:
#        paaris.append(arv)
#    else:
#        paaritud.append(arv)

#print("Paaris arvud on", paaris)
#print("Paaritud arvud on", paaritud)

#print("Paaris arvude summa on", sum(paaris))
#print("Paaritute arvude summa on", sum(paaritud))

 
# Harjutus 9.4

#for i in range(1, 43):
#    if i % 3 == 0 and i % 5 == 0:
#        print(str(i) + ' TIKTAK')
#    elif i % 5 == 0:
#        print(str(i) + ' TAK')
#    elif i % 3 == 0:
#        print(str(i) + ' TIK')
#    elif i % 3 != 0 or i % 5 != 0:
#        print(i)

# Harjutus 9.5

esimene = True

for i in range(200, 321):
    if i % 7 == 0 and arv % 5 != 0:
        if not esimene:
            print(", ", end="")
        print(arv, end="")
        esimene = False
