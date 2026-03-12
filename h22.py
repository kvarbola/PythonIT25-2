import datetime
import csv
# Lihtne kuupäev
# Kuva praegune päev, kuu, aasta, tund, minut

kp = datetime.datetime.now()
print(kp)

# Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S

print (kp.strftime("%d.%m.%Y,  %H:%M:%S"))

# Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled

msp = datetime.datetime(2009,7,8)

vanusp = kp - msp

print(f"Vanus päevades {vanusp}")

# Kuva vanus aastates

vanusa = vanusp.days // 365

print(f"Vanus aastates {vanusa}")

# Kuva, kas tegemist on juubeliaastaga

if vanusa%5 == 0:
    print("Sul on juubel!")
else:
    print("Sul ei ole juubel")

# Autorent
# Kasuta seda faili: rentals.csv
autode_arv = 0
kliendid = []
# Rentide arv – leia mitu renditehingut on tehtud

faili_nimi = 'rentals.csv'


with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    pais = next(csv_lugeja)

    for rida in csv_lugeja:
        autode_arv+=1
        if rida[7] not in kliendid:
            kliendid.append(rida[7])
        if rida[2] == rida[3]:
            
        
 

print(f"Renditehinguid kokku: {autode_arv}")

# Unikaalsed kliendid ja keskmine vanus – arvutage, mitu unikaalset klienti (customer ID) andmetes esineb ja mis on teie klientide keskmine vanus


print(f"Kliente kokku: {len(kliendid)}")

# Tagastamine – milline osakaal broneeringutest hõlmab risti-kontori rentimist, kus klient võtab auto ühest kohast ja tagastab selle teise kontorisse?

print(rida)

# Keskmine rentimise kestus – mis on keskmine rentimise kestus?