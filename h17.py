mehed_kokku = 0
mehed_tootunnid_kokku = 0
mehed_palk = 0

with open("palgad.txt") as fail:
    s = fail.readlines()
    for i in s:    
        tykeldus = i.split(",")
        if tykeldus[3] == "Mees":
            mehed_kokku += 1
    print(mehed_kokku)
    # tykeldus = rida.split(",")
    # for r in tykeldus:
    #     print(r, end=".")