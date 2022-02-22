A, B = str(input()), str(input())
aList, bList = A.split(), B.split()
print(f"{(((float(bList[0])-float(aList[0]))**2) + ((float(bList[1])-float(aList[1]))**2))**(0.5):.4f}")