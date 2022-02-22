x = str(input())
z = x.split()
y = list()
for n in range(len(z)):
    y.append(int(z[n]))

if (y[1]>y[2]) and (y[3]>y[0]) and ((y[2]+y[3])>(y[0]+y[1])) and (y[2]>0) and (y[3]>0) and (y[0]%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")