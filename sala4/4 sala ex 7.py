a = []
for i in range(10):
    a.append(int(input('escolha os valores da sua lista A:')))
b = []
for i in range(9, -1, -1):
    b.append(a[i])
for i in range(10):
    print(b[i])