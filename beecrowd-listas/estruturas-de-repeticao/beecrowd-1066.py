x0 = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

n = [x0,x1,x2,x3,x4]

p, i, pos, neg = 0, 0, 0, 0
for j in range(len(n)):
    if (abs(n[j]) % 2 == 0):
        p += 1
    if (abs(n[j]) % 2 == 1):
        i += 1
    if (n[j] > 0):
        pos += 1
    if (n[j] < 0):
        neg += 1

print(f"{p} valor(es) par(es)")
print(f"{i} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")