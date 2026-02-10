# 4.4

kylalised = int(input("Sisestage külaliste arv: "))
n = 1

def tervitus(a):
    global n
    print('Võõrustaja: "Tere!"')
    print(f"Täna {n}. kord tervitada, mõtiskleb võõrustaja")
    print('Külaline: "Tere, suur tänu kutse eest!"')
    n = n + 1
    return " "

for i in range(kylalised):
    print(tervitus(kylalised))

