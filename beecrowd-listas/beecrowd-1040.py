x = str(input())
xList = x.split()

n = list()
for i in range(len(xList)):
    n.append(float(xList[i]))

m = (2*n[0] + 3*n[1] + 4*n[2] + n[3])/10
print(f"Media: {m:.1f}")

if (m >= 7):
    print("Aluno aprovado.")
elif (m < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    ex = float(input())
    print(f"Nota do exame: {ex:.1f}")
    mf = (m + ex)/2

    if (mf >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {mf:.1f}")
