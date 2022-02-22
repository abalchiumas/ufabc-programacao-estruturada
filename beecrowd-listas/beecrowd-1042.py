x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(int(xList[i]))
n.sort()

for i in range(len(n)):
    print(n[i])

print("")

for j in range(len(xList)):
    print(int(xList[j]))
