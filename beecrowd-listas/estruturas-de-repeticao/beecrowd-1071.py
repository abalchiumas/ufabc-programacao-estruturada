x = int(input())
y = int(input())

if (x == y):
    print(0)
else:
    s = 0
    for i in range(min(x,y)+1,max(x,y),1):
        if (i % 2 == 1):
            s += i
    print(s)