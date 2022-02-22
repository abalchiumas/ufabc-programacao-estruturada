x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(float(xList[i]))
m = sorted(n, reverse=True)

if (m[0] >= m[1] + m[2]):
    print("NAO FORMA TRIANGULO")
else:
    if (m[0]**2 == m[1]**2 + m[2]**2):
        print("TRIANGULO RETANGULO")
    elif (m[0]**2 > m[1]**2 + m[2]**2):
        print("TRIANGULO OBTUSANGULO")
        if (m[0] == m[1] == m[2]):
            print("TRIANGULO EQUILATERO")
        if (m[0] == m[1] != m[2]) or (m[1] == m[2] != m[0]) or (m[0] == m[2] != m[1]):
            print("TRIANGULO ISOSCELES")
    else:
        print("TRIANGULO ACUTANGULO")
        if (m[0] == m[1] == m[2]):
            print("TRIANGULO EQUILATERO")
        if (m[0] == m[1] != m[2]) or (m[1] == m[2] != m[0]) or (m[0] == m[2] != m[1]):
            print("TRIANGULO ISOSCELES")