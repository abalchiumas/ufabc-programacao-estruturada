x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(float(xList[i]))

if (n[0] + n[1] > n[2]) and (n[0] + n[2] > n[1]) and (n[1] + n[2] > n[0]):
    print(f"Perimetro = {sum(n):.1f}")
else:
    print(f"Area = {(0.5)*(n[0]+n[1])*n[2]:.1f}")