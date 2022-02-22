lanche = {"1":4.00, "2":4.50, "3":5.00, "4":2.00, "5":1.50}

x = str(input())
xList = x.split()

print(f"Total: R$ {lanche[xList[0]]*int(xList[1]):.2f}")
