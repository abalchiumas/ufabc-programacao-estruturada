x = str(input())
y = x.split()
z = list()
for n in range(len(y)):
    z.append(float(y[n]))

delta = (z[1]**2) - (4*z[0]*z[2])

if (z[0] == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    x1 = ((-1)*z[1] + (delta**0.5))/(2*z[0])
    x2 = ((-1)*z[1] - (delta**0.5))/(2*z[0])

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")