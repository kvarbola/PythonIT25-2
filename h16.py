from datetime import date
import os

# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel

print(f"Hello {os.getlogin()}")

# Skript kuvab kasutajale praeguse töökataloogi tee

print(f"Sinu kataloogitee: {os.getcwd()}")

# Kataloogide loomine:
    # Skript küsib kasutajalt, mitu kataloogi ta soovib luua

today = date.today()
try:
    os.mkdir(str(today))
except:
    print("Ära jama, juba olemas.")

# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

mitu = int(input("Mitu kataloogi soovid luua: "))
for i in range(mitu):
    os.mkdir(str(today)+"/"+str(i+1))
    print(f"Kataloogid 1-{mitu} tehtud")

# Kataloogi kustutamine:
    # Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne

kustuta = input(f"Kustuta valikust 1-{mitu}:")
path = os.getcwd()+"\\"+str(today)+"\\"+kustuta
if os.path.isdir(path):
    os.rmdir(path)