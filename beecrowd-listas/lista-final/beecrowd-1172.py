def subsVetor(n:list):
    for i in range(len(n)):
        if n[i] <= 0:
            n[i] = 1

    for j in range(len(n)):
        print(f"X[{j}] = {n[j]}")

lista = list()
for k in range(10):
    x = int(input())
    lista.append(x)

subsVetor(lista)