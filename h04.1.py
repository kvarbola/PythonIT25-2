#    4. Ülesanne
#    Raamatupoes on 30% soodusmüük.
#    Kirjuta programm, mis küsib kasutajalt soovitud raamatute arvu ja arvutab nende kogumaksumuse, kui iga raamatu tavahind on 12,53€.
#    Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
#    Näide:
#    Kasutaja sisestab: 3
#    Programm väljastab: 3 raamatu hind soodustusega on 26.25€.


ale = 0.3
raamatute_arv = int(input("soovitud raamatute arv: "))
hind = 12.53
summa = raamatute_arv * (hind-hind*ale)

print(f"{raamatute_arv} raamatu hind soodustusega on {summa:0.2f}€")