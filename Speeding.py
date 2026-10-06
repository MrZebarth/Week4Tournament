def caught_speeding(speed, is_birthday):
    print(isinstance(speed,(float,str)))
    if is_birthday==True:
        speed-=5
    if speed<=60:
        return 0
    elif 61<=speed<=80:
        return 1
    else:
        return 2
print(caught_speeding(65, True))