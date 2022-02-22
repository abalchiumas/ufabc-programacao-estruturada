x0 = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

n = [x0,x1,x2,x3,x4]

i = 0
for j in range(len(n)):
    if (abs(n[j]) % 2 == 0):
        i += 1

print(f"{i} valores pares")