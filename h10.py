#Harjutus 10

import random

arv = random.randint(1,3)
katse = 0


for i in range(10):
    v = int(input("Paku arv: "))
    
    if arv==v:
        print("Arvasid õigesti!")
        katse+=1
        arv = random.randint(1,3)
    else:
        print("Arvasid valesti")
print(f"skoor: {katse}")
        