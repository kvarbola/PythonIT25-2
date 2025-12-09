#kordamine

#1.Kellaaeg

tunnid = 2
minutid = 38
sekundid = 59

#print(tunnid,":",minutid,":",sekundid,"PM")

#2.Tsitaat lause sees

Tsitaat = "'Üks kord me võidame niikuinii' - Heinz"

#print(Tsitaat)

#3.Mallide kasutamine

eesnimi = "Jüri"
perenimi = "Jurakas"

#print(eesnimi,perenimi,"nimetähed on",eesnimi.strip("üri")+"."+perenimi.strip("urakas"))

#4.Perenime pikkus

pe = "varbola, kauri"
pe2 = pe.split(", ")
print()



#5.E-posti aadressi muutmine

email = "kvarbola@hkhk.edu.ee"

#print(email.replace("hkhk.edu.ee","gmail.com"))

#6.Andmerida analüüs

andmed = "1,Marshal,Martinovic,mmartinovic0@dedecms.com,Male,40.19.226.175"




#7.Sõidu aeg ja kaugus

sõidu_kaugus = 220
kiirus = 90
sõiduaeg = round(sõidu_kaugus/kiirus)

#print(sõiduaeg,"h")


#8.Posituse kuvamine

postitused=137
lk=round(postitused/10)
viimane=postitused%10
#if viimane==0:
 #   print(10)
#else:
 #   print(viimane)
#print(lk)

#9.Serveri töökulu
 
võimsus=400
kWh=võimsus/1000*60
hind=9.69*kWh/100

#print(hind,"€")

#10.Sõna- ja massiivioperatsioonid nädalapäevadega

massiiv = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede"]

reverse=True
print(len(massiiv))
print(massiiv)





















