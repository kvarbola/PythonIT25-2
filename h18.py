import csv

faili_nimi = 'EstonianBasketballGames.csv'
meeskonnad = []
mk_mangud = {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    # Päise (header) lugemine
    pais = next(csv_lugeja)

    # print(f"Päise veerud: {pais}")
    for rida in csv_lugeja:
        # print(rida[1], rida[2])
        if rida[1] not in meeskonnad:
            meeskonnad.append(rida[1])
            mk_mangud[rida[1]] = 1
        else:
            mk_mangud[rida[1]] += 1
        if rida[2] not in meeskonnad:
            meeskonnad.append(rida[2])
            mk_mangud[rida[2]] = 1
        else:
            mk_mangud[rida[2]] += 1
        
print("Meeskondasid kokku:", len(meeskonnad))
for mk in meeskonnad:
    print(mk)

print(mk_mangud)

# Kuva mitu meeskonda osales