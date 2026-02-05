fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))

fail.close()
