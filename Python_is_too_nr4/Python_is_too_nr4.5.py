# 4.5 mündid

nimi = input("Sisesta failinimi: ")

def pronksikarva_summa(a):
    fail = open("mündid.txt", encoding="UTF-8")
    
    for rida in fail:
        print(rida)
    return "lõpp"

pronksikarva_summa(nimi)