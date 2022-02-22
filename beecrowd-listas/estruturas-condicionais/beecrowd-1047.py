x = str(input())
xList = x.split()
d0 = [int(xList[0]),int(xList[1])]
d1 = [int(xList[2]),int(xList[3])]

if (d0[0] == d1[0]):
    if (d0[1] == d1[1]):
        h, m = 24, 0
    elif (d0[1] > d1[1]):
        h, m = 23, (60 - (d0[1] - d1[1]))
    else:
        h, m = 0, (d1[1] - d0[1])
else:
    if(d0[0] > d1[0]):
        total = abs((((d1[0] + 24) * 60) + d1[1]) - ((d0[0] * 60) + d0[1]))
    else:
        total = abs((((d1[0]) * 60) + d1[1]) - ((d0[0] * 60) + d0[1]))
    h = total // 60
    m = total - (h * 60)

print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")