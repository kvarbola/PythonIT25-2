# funktsioon dokumentatsioooniga
# C > F

def tempteisendamine(t, k):
    
    """
    
    teisendab F C-ks ja vastupidi
    
    Parameetrid:
    c (str): kraad.
    b (int): temperatuur.

    Tagastab:
    Teisendatud arvu.
    
    """
    
    if t == "c":
        #F leidmine
        vastus = k * 9/5 + 32
    elif t == "f":
        #C leidmine
        vastus = (k - 32) / (9/5)
    else:
        #Ei saanud aru
        vastus = "Ma ei mõista sind"
    print(vastus)

tempteisendamine("c", 32)
print(tempteisendamine.__doc__)