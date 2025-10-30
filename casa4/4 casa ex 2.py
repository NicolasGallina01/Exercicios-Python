a = []
for i in range(9):
    a.append(int(input('escolha os valores da sua lista RA:')))
b = []
for i in range(5):
    b.append(a[i])
for i in range(8, 4, -1):
    b.append(a[i])
print(b)