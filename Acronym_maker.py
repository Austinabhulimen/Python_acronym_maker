def change_word(name):
    r =[]
    for i in name:
        if " " in name:
            r = name.rsplit(" ")

    a = 0
    value = []
    p = []

    l = len(r)

    while a < l:
        y = r.pop(0)
        value.append( y[0].upper())
        p.append(y)
        p.clear()
        a+=1

    for z in value:
        print(z, end = ' ')


change_word(name = input('please enter your name in full: ').lower())