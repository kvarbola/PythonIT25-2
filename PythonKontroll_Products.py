# Kauri Varbola 25.03.2026 Python kontrolltöö Products.

import requests

yl = "products"
url = f"https://dummyjson.com/{yl}"
response = requests.get(url)
hinnad = []
KallimNimi = []
laoseis =[]
koguhind = 0


if response.status_code == 200:
    data = response.json()

    print("--------TOOTED--------")
    for line in data[yl]:
        hinnad.append(line['price'])
        koguhind += line['price']

        print(f"Toode: {line['title']}€")
        print(f"Hind: {line['price']}€")
        print("-----")

    for line in data[yl]:
        if line['price'] == max(hinnad):
            KallimNimi.append(line['title'])

    print(f"Kallim toode on {KallimNimi[0]}. Hind: {max(hinnad)}€")
    print(" ")

    print("----LAOSEIS ALLA 20NE----")
    for line in data[yl]:
        if line['stock'] < 20:
            print(line['title'])
            print("-----")
            
    keskmine = koguhind / len(hinnad)
    print(f"Toodete keskmine hind on {round(keskmine)}€")

        
else:
    print(response.status_code)
