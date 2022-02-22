n = int(input())
i = 0
x_vals = list()

while i < n:
    x = int(input())
    x_vals.append(x)
    i += 1

c = 0
for j in range(len(x_vals)):
    if (10 <= x_vals[j] <= 20):
        c += 1

print(f"{c} in")
print(f"{len(x_vals)-c} out")