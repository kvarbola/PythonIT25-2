# 4.6

kuupaev = str(input("Sisesta kuupäev formaadis DD.MM.YYYY: "))

def kuu_sonana(a):
    
    kuud = ["Vali kuu","jaanuar","veebruar","märts","april","mai","juuni","juuli","august","september","oktoober","november","detsember"]

    x = kuupaev.split(".")

    print(f"{int(x[0])}.{kuud[int(x[1])]} {int(x[2])}")
    
kuu_sonana(kuupaev)