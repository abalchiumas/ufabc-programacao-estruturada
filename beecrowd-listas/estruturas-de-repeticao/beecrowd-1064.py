x0 = float(input())
x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
x5 = float(input())

n = [x0,x1,x2,x3,x4,x5]

i, m = 0, 0
for j in range(len(n)):
    if (n[j] > 0):
        i += 1
        m += n[j]

print(f"{i} valores positivos")
print(f"{m/i:.1f}")