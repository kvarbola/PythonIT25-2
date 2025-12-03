# 03.12.20205 Kauri Varbola



#07.2

mootmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {mootmised[0]}")
print(f"Viimane mõõdetav tulemus: {mootmised[-1]} kraadi")
print(f"Kõik tempid: {mootmised[1:]}")
print(f"Maksimaalne temperatuur: {max(mootmised[1:])}")
print(f"Minimaalne temperatuur: {min(mootmised[1:])}")
print(f"Keskmine temperatuur: {round(sum(mootmised[1:])/len(mootmised[1:]),1)}")

print(f"-20 esineb: {mootmised[1:].count(-20)} korda")
del mootmised[4]
mootmised.insert(4,16)
mootmised[1:].sort()
print(mootmised)



# 07.1
# loendist otsimine: vasak -> (0,1,2,3...). parem <- (-1,-2,-3...)
playlist = ['1. ALIKA – "Bridges"',
            '2. Anett x Fredi – "Read Between The Lines"',
            '3. villemdrillem – "leekiv armastus"',
            '4. Clicherik & Mäx – "PAKSUD"',
            '5. nublu – "ära ärata"',
            '6. NOËP – "Move Your Feet"',
            '7. Trad.Attack! – "Bring It On"',
            '8. Bedwetters – "It Is What It Is"',
            '9. Reket – "Panama paberid"',
            '10. Grete Paia – "Võluväel"']

#print(playlist)
#valik = int(input("Vali lugu: "))
#print(playlist[valik-1])