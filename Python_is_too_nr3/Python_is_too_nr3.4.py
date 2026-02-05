# 3.4

valik = "jukebox.txt"
nr = 1

fail = open(valik, encoding="UTF-8")

for rida in fail:
    print(nr, rida)
    nr += 1

fail.seek(0)   
nr = 1

otsus = int(input("Millist laulu tahad?: "))

for rida in fail:
    if otsus == nr:
        print(nr, rida)
    nr += 1


fail.close()