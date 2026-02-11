# 4.5 mündid

nimi = input("Sisesta failinimi: ")
summa = 0

def pronksikarva_summa(a):
    global summa
    
    fail = open("mündid.txt", encoding="UTF-8")
    
    for rida in fail:
        if int(rida) <= 5:
            summa += int(rida)
    print(summa)

pronksikarva_summa(nimi)