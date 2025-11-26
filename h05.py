#Kauri
#26.11.2025

# ündiviskamise äraarvamine koos
# Juhuslikkusega (and ja or)
# 0 = kiri
# 1 = kull
import random

mynt = random.randint(0,1)
arvamus = int(input("Kull või kiri (0/1): "))
print(f"Münt: {mynt}")
print(f"Arvamus: {arvamus}")
if mynt == arvamus:
    print("Võit!")
else:
    print("Kaotus...")



#Ilmaennusutuse rakendus (and)

#try:
#    temp = int(input("Sistesta kraadid C: "))
#    if temp < 0:
#        print("talveriided")
#    elif temp >= 0 and temp <= 15:
#        print("kevad-sügisriided")
#    else:
#        print("suveriided")
#    
#except:
#    print("Urror - määää")