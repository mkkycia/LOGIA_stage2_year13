def kiedy(dzien, noc, polki):
    lista = []
    for i in range(0, 1000, polki):
        lista.append(i)
    wysokosc = 0
    doba = 0
    bylo = False
    while True:
        doba += 1
        wysokosc += dzien
        if wysokosc > 999:
            return doba
        for i in range(wysokosc, wysokosc-noc, -1):
            if i in lista:
                wysokosc = i
                bylo = True
                break
        if bylo == False:
            wysokosc -= noc
        bylo = False

print(kiedy(5, 3, 2))
        
