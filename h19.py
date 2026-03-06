import json


with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

kl12 = 0
kl11 = 0
kl10 = 0

for tul in tulemused:
    if tul['klass'] == '12':
        print(tul['nimi'])
        for teg in tul['tegevused']:
            print("\t", teg)
        print("------------HINNETELEHT------------")
        # print(tul['hinded'])
        for y in tul['hinded']:
            print (y,':',tul['hinded'][y])
        kl12 += 1
    elif tul['klass'] == '11':
        kl11 += 1
    else:
        kl10 += 1

print("-----------------------------------")
print(f"12.klassis õpib {kl12} õpilast")
print(f"11.klassis õpib {kl11} õpilast")
print(f"10.klassis õpib {kl10} õpilast")