def evenOdd(x:int):
    if (x % 2 == 0):
        return "EVEN"
    else:
        return "ODD"

def checker(x:int):
    if (x == 0):
        return "NULL"
    elif (x > 0):
        return evenOdd(x) + " POSITIVE"
    else:
        return evenOdd(x) + " NEGATIVE"

n = int(input())
for i in range(n):
    x = int(input())
    print(checker(x))