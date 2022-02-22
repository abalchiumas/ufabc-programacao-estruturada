x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(float(xList[i]))

if (n[0] == 0) and (n[1] == 0):
    print("Origem")
elif (n[0] == 0) and (n[1] != 0):
    print("Eixo Y")
elif (n[0] != 0) and (n[1] == 0):
    print("Eixo X")
elif (n[0] > 0):
    if(n[1] > 0):
        print("Q1")
    else:
        print("Q4")
else:
    if (n[1] > 0):
        print("Q2")
    else:
        print("Q3")