# n = list()
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for i in range(len(n)):
#     x = int(input())
#     return

def trocaVetor(n:list):
    for i in range(len(n)):
        tmp1 = n
        tmp2 = list()
        n[i] = n[len(n)-i-1]
        n[len(n)-i-1] = tmp1
        print(f"N[{i}] = {n[i]}")

print(trocaVetor(n))