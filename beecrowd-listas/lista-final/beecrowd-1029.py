def fib(n:int):
    f0 = 0
    f1 = 1
    for i in range(n):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f"fib({n}) = {2*(f2-1)} calls = {f1+f0-f2}"

n = int(input())
for i in range(n):
    x = int(input())
    print(fib(x))