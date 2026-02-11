#pank depo ja väljavõte

def depo(s, r):
    
    """
    lisab raha kontole
    
    Parameetrid:
    s (int): saldo.
    b (int): raha.

    Tagastab:
    uue summa.
    """
    
    uus = s + r
    return uus
    

saldo = 100

def vv(s, r):
    
    """
    võtab kontolt raha
    
    Parameetrid:
    s (int): saldo.
    b (int): raha.

    Tagastab:
    uue summa.
    """
    
    uus = s - r
    return uus

print(saldo)
saldo = depo(saldo, 10)
saldo = depo(saldo, 100)
saldo = depo(saldo, 10000)
saldo = depo(saldo, 10.5)
saldo = depo(saldo, 1.5)
saldo = depo(saldo, 63)
saldo = depo(saldo, 1)
print(depo.__doc__)
print(saldo)
saldo = vv(saldo, 6)
print(vv.__doc__)
print(saldo)


