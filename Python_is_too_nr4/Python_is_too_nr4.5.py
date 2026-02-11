# 4.5 mündid

nimi = input("Sisesta failinimi: ")
summa = 0

def pronksikarva_summa(a):
    global summa
    global nimi
    
    fail = open("mündid.txt", encoding="UTF-8")
    if nimi == "mündid.txt":
        for rida in fail:
            if int(rida) <= 5:
                summa += int(rida)
        print(f"Hoiupõrsasse läheb {summa} senti.")
    else:
        print("Faili ei leitud!")

pronksikarva_summa(nimi)