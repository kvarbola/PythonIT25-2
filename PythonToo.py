inim = 41
kohad = 40

tais = inim // kohad
jaak = inim % kohad
if jaak > 0:
    lisa = 1
else:
    lisa = 0
bussid = tais + lisa


print(f"Täis: {tais}")
print(f"Viimases: {jaak}")
print(f"Busse kokku: {bussid}")


print("Tere, maailm!")
aasta = str(2020)
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = aasta+lause_keskosa+liblikas 

print(lause)
#pilved
#korgus = float(input("Pilvede aluse kõrgus km: "))
#print(type(korgus))
#Kui pilvede kõrgus on suurem kui 6.0
#if korgus > 6.0:
#    print("Need on ülemised pilved")
#else:
 #   print("Need ei ole ülemised pilved")