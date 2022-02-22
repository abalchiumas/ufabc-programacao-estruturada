x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(int(xList[i]))

total = (((n[2]*60)+n[3])-((n[0]*60)+n[1]))

if (1 <= total <= 24*60):
    if (total < 60):
        h = 0
        m = total
    else:
        if (n[0] == n[2]) and (n[1] == n[3]):
            h = 24
            m = 0
        else:
            h = total % 60
            m = total-60*(n[2]-n[0])
    print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")