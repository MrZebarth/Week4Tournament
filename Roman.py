text = input()

total = 0
i=0
while i<len(text):
    if text[i]=="I":
        if i<len(text)-1:
            if text[i+1]=="V":
                total+=4
                i+=1
            elif text[i+1]=="X":
                total+=9
                i+=1
            else:
                total+=1
        else:
            total+=1
    elif text[i]=="V":
        total+=5
    elif text[i]=="X":
        if i<len(text)-1:
            if text[i+1]=="L":
                total+=40
                i+=1
            elif text[i+1]=="C":
                total+=90
                i+=1
            else:
                total+=10
        else:
            total+=10
    elif text[i]=="L":
        total+=50
    elif text[i]=="C":
        if i<len(text)-1:
            if text[i+1]=="D":
                total+=400
                i+=1
            elif text[i+1]=="M":
                total+=900
                i+=1
            else:
                total+=100
        else:
            total+=100
    elif text[i]=="D":
        total+=500
    elif text[i]=="M":
        total+=1000
    i+=1
print(total)