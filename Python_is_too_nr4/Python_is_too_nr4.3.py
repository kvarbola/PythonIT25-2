# 4.3

kutsutud = int(input("Mitu külalist on kutsutud?: "))
tulevad = int(input("Mitu külalist tulevad?: "))

def eelarve(a):
    kogusumma = a * 10 + 55
    return kogusumma

print("Maksimaalne eelarve:", eelarve(kutsutud), "eurot")
print("Minimaalne eelarve:", eelarve(tulevad), "eurot")



