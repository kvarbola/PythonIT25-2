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

#esimene = True

#for i in range(200, 321):
#    if i % 7 == 0 and arv % 5 != 0:
#        if not esimene:
#            print(", ", end="")
#        print(arv, end="")
#        esimene = False

# Harjutus 9.8

#for i in range(11):
#    print(f"{i} * {i} = {i*i}")

# Harjutus 9.9 , 9.10

# import random
# tehe = ["+","-","*","/"]
# p = 0
# kysimuste_arv = 1
# 
# for _ in range(kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
#     
#     if t=="+":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("vastus: "))
#         if arv1+arv2 == v:
#             p+=1
#     elif t=="-":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("vastus: "))
#         if arv1-arv2 == v:
#             p+=1
#     elif t=="*":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("vastus: "))
#         if arv1*arv2 == v:
#             p+=1
#     else:
#         print(f"{arv1}{t}{arv2}=")
#         v = float(input("vastus: "))
#         if arv1/arv2 == v:
#             p+=1
# print(p)
# if p/kysimuste_arv >= 0.5:
#     print(f"A - {p}/{kysimuste_arv}")
# else:
#     print("MA - {p}/{kysimuste_arv}")

#Harjutus 9.11

#1
arv = 5
for i in range(1,6):
    print(" "*i+ "*" * arv)
    arv-=1

#2
arv = 5
for i in range(1,6):
    print("*" * arv)
    arv-=1

#3
arv = 5
for i in range(1,6):
    print(" " * arv + "*" * i)
    arv-=1

#4
arv = 5
for i in range(1,6):
    print("*" * i)