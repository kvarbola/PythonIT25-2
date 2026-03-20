#8. arved.json
# 	Leia makstud ja tasumata arvete arv.
#	Leia kogusumma kõikidest makstud arvetest.
#	Leia keskmine arvete summa.
#	Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
#	Loetle kõik tasumata arved, mille tähtaeg on juba möödunud.

import requests
import datetime

yl = "arved"
url = f"https://metshein.com/kordamine/json/{yl}.json"
response = requests.get(url)

kliendid = 0
makstud = 0
maksmata = 0
summa = 0
summa2 = 0
moodunud = 0
if response.status_code == 200:
    data = response.json()

    for arve in data[yl]:
        if arve['makstud']:
            makstud+=1
            summa+=round(arve['summa'])
        else:
            maksmata+=1
            if arve['tähtaeg'] != datetime.datetime.today():
                moodunud+=1
    
    for arve in data[yl]:
        kliendid+=1
        summa2+=arve['summa']
    kesk = summa2
    kesk/=kliendid

    print(f"Makstud arveid on: {makstud}")
    print(f"Maksmata arveid on: {maksmata}")
    print(f"Makstud arvete summa on: {summa}€")
    print(f"Keskmine arvete summa on: {round(kesk)}€")
    print(f"Möödunud tähtajage tasumata arveid on: {moodunud}")
else:
    print(response.status_code)

